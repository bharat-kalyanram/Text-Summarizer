import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "text-summarizer"

list_of_files = [
    #use: whenever we have to do the CI/CD deployment, this will automatically take your code from github and deploy
    #.gitkeep is a hidden file created so that when committed empty folder isn't uploaded 
    ".github/workflows/.gitkeep",
    #__init__.py is a constructor file - to install a local package
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.py"

]

for filepath in list_of_files:
    #to handle '\' and '/' issue in linux and windows
    filepath = Path(filepath)
    #to split path name into folder name and file name 
    filedir, filename = os.path.split(filepath)
    #run only if filedir is empty such that a folder will be created if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for he file {filename}")
    #creating a file in case the file size if 0
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
    else:
        logging.info(f"{filename} already exists")
         