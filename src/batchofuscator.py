from os import listdir
from os.path import isfile, join
from typing import List
from PyObfuscator import Obfuscator, Name
from src.generics.utils_functions import get_config_file_data
config,config_file = get_config_file_data()
config.read(config_file)
PASSWORD:str = config._defaults['encryption_password']

def launch_batch_ofuscator(path):
    python_files:List[str] = []
    onlyfiles = [f for f in listdir(path[-1]) if isfile(join(path[-1], f))]
    for file in onlyfiles:
        if('.py' in file):
            python_files.append(file)
            ofuscateFile(file)
    print('Encrypted files: '+str(python_files))

def ofuscateFile(file):
    new_file_name:str = file.split('.py')[0]+"__obfu__.py"
    print('New file: '+new_file_name)
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
    config._defaults['encryption_password'],
    "utf-8",
    8,
    ).default_obfuscation()
