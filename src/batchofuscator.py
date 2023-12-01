from os import listdir
from os.path import isfile, join
from typing import List
from PyObfuscator import Obfuscator, Name

def launch_batch_ofuscator(path):
    python_files:List[str] = []
    onlyfiles = [f for f in listdir(path[-1]) if isfile(join(path[-1], f))]
    for file in onlyfiles:
        if('.py' in file):
            python_files.append(file)
            ofuscateFile(file)
    print(python_files)
    return True

def ofuscateFile(file):
    new_file_name:str = file.split('.py')[0]+"obfu.py"
    Obfuscator(
    file,
    new_file_name,
    6,
    {
        "name1": Name("name1", "obfu_name1", False, None),
        "name2": Name("name2", "obfu_name2", False, None),
        "name3": Name("name3", "obfu_name3", False, None),
    },
    True,
    "mypassword",
    "utf-8",
    8,
    ).default_obfuscation()
