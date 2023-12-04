import os
from configparser import ConfigParser
import pathlib
import platform
import shutil

def get_config_file_data():
    os_platform = platform.platform()
    separator ='/'
    if('Windows' in os_platform):
        separator = '\\'

    abs_path = os.path.abspath(__file__).split(separator)
    src_position = abs_path.index("src")

    config_file_path:str =  separator.join(abs_path[:src_position])
    config_file = config_file_path + separator +'config.cfg'
    config = ConfigParser()

    return config,config_file

def callbackIgnore(paths):
      """ callback for shutil.copytree """
      def ignoref(directory, contents):
          arr = [] 
          for f in contents:
              for p in paths:
                  if (pathlib.PurePath(directory, f).match(p)):
                      arr.append(f)
          return arr
  
      return ignoref

def copy_path(from_path, to_path):
    paths_to_ignore = ['.git','env','.vscode','.gitignore']
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path,ignore=callbackIgnore(paths_to_ignore))