import os
from pathlib import Path
import logging
import sys
from Exception.logger import logging
from Exception.exception import CustomException


# logging.basicConfig(level=logging.INFO)


project_name = "AI_Medical_ChatBot_using_LLM"

list_of_files = [
    # ".github/workflows/.gitkeep",
    f"src/init.py",
    f"src/helper.py",
    f"src/prompt.py",
    f"experiment/test.ipynb",
    "Exception/logger.py",
    "Exception/exception.py",
    "main.py",
    "requirements.txt",
    "setup.py",
    "app.py",
    "store_index.py",
    "statics/.gitkeep",
    "Templates/chat.html"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
