import os
import configparser

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'config.ini')
config = configparser.ConfigParser()
f = open(file_path, 'r')
config.readfp(f)
username = config.get("Client", "account")
password = config.get("Client", "password")
