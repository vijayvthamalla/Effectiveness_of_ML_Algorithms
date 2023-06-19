import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d %(message)s]')

project_name = "Project_name"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/logging/logging.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/pipeline.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/constants.py",
    f"src/{project_name}/dev/test.ipynb",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "README.md",
]

for filename in list_of_files:
    filepath = Path(filename)
    filedir, filename = os.path.split(filepath)
    if not os.path.exists(filepath):
        logging.info(f"Creating {filepath}")
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
        filepath.touch()
        logging.info(f"Created {filepath}")