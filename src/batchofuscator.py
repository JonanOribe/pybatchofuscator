from os import listdir
import os
from os.path import isfile, join
from typing import List
from PyObfuscator import Obfuscator, Name
from src.generics.utils_functions import copy_path, get_config_file_data
config,config_file = get_config_file_data()
config.read(config_file)
PASSWORD:str = config._defaults['encryption_password']
dist_path = "/dist/"

def launch_batch_ofuscator(path):
    final_dist_path:str = path[-1]+dist_path
    create_dist_path(dist_path)
    python_files:List[str] = []
    copy_path(path[-1],final_dist_path)
    onlyfiles = [f for f in listdir(path[-1]) if isfile(join(final_dist_path, f))]
    for file in onlyfiles:
        if('.py' in file):
            python_files.append(file)
            ofuscateFile(file)
    print('Encrypted files: '+str(python_files))

def ofuscateFile(file):
    old_file:str = './dist/'+file
    new_file_name:str = './dist/'+file.split('.py')[0]+"__obfu__.py"
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
    os.remove(old_file)

def create_dist_path(path):
    if(os.path.exists(path)!=True):
        os.makedirs(path)
        print("The new directory is created! You will find your encrypted files in: "+path)
       