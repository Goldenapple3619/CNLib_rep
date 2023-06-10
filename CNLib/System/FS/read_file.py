from os.path import isfile
from typing import TextIO

def read_file(path: str, read_bytes: bool = False) -> str:
    if (not isfile(path)):
        raise FileNotFoundError()

    fp: TextIO = open(path, 'rb' if read_bytes else 'r', errors="ignore")

    if (not fp.readable()):
        fp.close()
        raise PermissionError()

    text: str = fp.read()
    fp.close()

    return (text)
