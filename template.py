import os 
from pathlib import Path
import logging 


logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s:')

project_name =  "mlProject"

list_of_files = [
    f"sercets/{project_name}/__init__.py",
    f"sercets/{project_name}/components/__init__.py",   
    f"sercets/{project_name}/utils/__init__.py",
    f"sercets/{project_name}/utils/common.py",
    f"sercets/{project_name}/config/__init__.py",       
    f"sercets/{project_name}/config/configuration.py",
    f"sercets/{project_name}/pipeline/__init__.py",
    f"sercets/{project_name}/entity/__init__.py",
    f"sercets/{project_name}/entity/config_entity.py",
    f"sercets/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",

]


for filepath in list_of_files :
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "" :
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"created directory : {filedir} for file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0) :
        with open (filepath, "w") as f :
            pass
            logging.info(f"created empty file : {filepath}")

    else:
        logging.info(f"{filename} is already exists")






