import os 
from box.exceptions import BoxValueError
import yaml
from mlProject import logger 
import json 
import joblib
from ensure import ensure_annotations
from box import CConfigBox
from pathlib import Path
from typing import Any




@ensure_annotations
def read_yaml(path_to_yaml: Path) -> CConfigBox:
    """Reads a yaml file and returns CConfigBox type object

    Args:
        path_to_yaml (Path): Path to the yaml file

    Returns:
        CConfigBox: ConfigBox type object
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return CConfigBox(content)
    except BoxValueError as e:
        raise e
    except Exception as e:
        logger.error(f"Error occurred while reading yaml file: {e}")
        raise e
    




@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates list of directories

    Args:
        path_to_directories (list): List of directory paths
        verbose (bool, optional): Whether to log info messages. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")





@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data to a json file

    Args:
        path (Path): Path to the json file
        data (dict): Data to be saved
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"Json file saved at: {path}")






@ensure_annotations
def load_json(path: Path) -> CConfigBox:
    """Loads data from a json file

    Args:
        path (Path): Path to the json file

    Returns:
        CConfigBox: ConfigBox type object
    """
    with open(path, "r") as json_file:
        content = json.load(json_file)
    logger.info(f"Json file loaded from: {path}")
    return CConfigBox(content)






@ensure_annotations
def save_bin(data: Any, path : Path):
    """Saves a python object to a file using joblib

    Args:
        path (Path): Path to the file
        obj (Any): Python object to be saved
    """
    joblib.dump(data, path)
    logger.info(f"Object saved at: {path}")






@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads a python object from a file using joblib

    Args:
        path (Path): Path to the file   
    Returns:
        Any: Loaded python object
    """
    data = joblib.load(path)
    logger.info(f"Object loaded from: {path}")
    return data







@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB

    Args:
        path (Path): Path to the file

    Returns:
        str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    logger.info(f"File size of {path} is {size_in_kb} KB")
    return f"{size_in_kb} KB"