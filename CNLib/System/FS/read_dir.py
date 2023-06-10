from os import (listdir, walk)
from os.path import (isfile, isdir)

def get_files_from_dir(path: str) -> list:
    return [path + '/' + item for item in listdir(path) if isfile(path + '/' + item)]

def get_folders_from_dir(path: str) -> list:
    return [path + '/' + item for item in listdir(path) if isdir(path + '/' + item)]

def get_files_from_subdirs(path: str) -> list:
    return [item[0] + "/" + file  for item in walk(path) for file in item[2]]

def get_folders_from_subdirs(path: str) -> list:
    return [item[0] + "/" + folder  for item in walk(path) for folder in item[1]]

def get_all_from_subdirs(path: str) -> list:
    return [item[0] + "/" + obj  for item in walk(path) for obj in item[1] + item[2]]
