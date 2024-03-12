import os
from pathlib import Path
import logging

# To see Information level logs in the terminal with time and message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

project_name = "main_project"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "reserach/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    # In the above list we gave forward slash but windows system accept backward slash so Path() function will take care of this 
    filepath = Path(filepath)
    ## Spliting directories and Files
    filedir, filename = os.path.split(filepath)
    #print(filename)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")

