from os.path import isfile
from typing import TextIO
from sys import stdin

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

def read_bytes(fp: TextIO, size: int, byte_order: str = 'little') -> int:
    if (fp.closed):
        raise PermissionError()

    if (not fp.readable()):
        fp.close()
        raise PermissionError()

    data: bytes = fp.read(size)

    if (isinstance(data, str)):
        data: bytes = data.encode()

    data: int = int.from_bytes(data, byte_order)

    return (data)
