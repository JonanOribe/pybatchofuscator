import sys, os
from configparser import ConfigParser

PROYECT_PATH=os.getcwd()
sys.path.insert(0, PROYECT_PATH + '/src/')

config = ConfigParser()
config.read('config.cfg')
