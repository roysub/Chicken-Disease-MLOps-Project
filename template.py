import os
from pathlib import Path
import logging

##Prepare Logging
##Initialise Log at basic level, Log current time and the message you want to put
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

##Project name {Change accordingly}
project_name = "chicken_disease_classifier"

##List of Folders you want to create
## this folder for the CI/CD pipeline (.github) in main.yaml file
## One for workflows
## .gitkeep file in the folder - so that if folder is empty, because of this file it will reflect in github 
##**Keep adding filenames/Folders in the List to create folders and run this file**
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py"
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml", ##parameters
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb" ##for research trials,
    "templates/index.html"
]

for filePath in list_of_files:    
    ##Reason - Because filepath here in Array is /, but Windows works with \. 
    #So Path takes care of these things according to OS
    filePath = Path(filePath)

    ##Need to separate Folder from files in the Filepath
    fileDir, fileName = os.path.split(filePath)

    if fileDir:
        ##Check if directory is not empty
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"Creating file directory; {fileDir} for the file ; {fileName}")

    ##Create files
    ## check if the filepath is empty and the filepath contains no files (0kb memory)    
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
        with open(filePath, "w") as f:
            logging.info(f"Creating empty file: (filepath)")
    else:
        logging.info(f"{fileName} is exists")
        
    



