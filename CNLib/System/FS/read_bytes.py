from typing import TextIO

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
