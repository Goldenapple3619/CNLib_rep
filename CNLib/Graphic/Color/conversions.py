from numbers import Number
from typing import Iterable

def hex_to_rgb(hex_color: str) -> tuple:
    if (not isinstance(hex_color, Iterable)):
        raise TypeError()

    if (hex_color.startswith('#')):
        hex_color = hex_color[1:]

    hex_color: str = hex_color.lower()
    temp_hex_color: str = hex_color.replace('a', '').replace('b', '').replace('c', '') \
        .replace('d', '').replace('e', '').replace('f', '')

    if (not temp_hex_color.isnumeric() and temp_hex_color != ''):
        raise (BaseException())

    if (len(hex_color) > 6):
        raise (ValueError())
    if (len(hex_color) < 6):
        hex_color += '0' * (6 - len(hex_color))

    return ((int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)))

def hex_to_rgba(hex_color: str) -> tuple:
    if (not isinstance(hex_color, Iterable)):
        raise TypeError()

    if (hex_color.startswith('#')):
        hex_color = hex_color[1:]

    hex_color: str = hex_color.lower()
    temp_hex_color: str = hex_color.replace('a', '').replace('b', '').replace('c', '') \
        .replace('d', '').replace('e', '').replace('f', '')

    if (not temp_hex_color.isnumeric() and temp_hex_color != ''):
        raise (BaseException())

    if (len(hex_color) > 8):
        raise (ValueError())
    if (len(hex_color) < 8):
        hex_color += '0' * (8 - len(hex_color))

    return ((int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16), int(hex_color[6:8], 16)))

def rgb_to_hex(r: int = 0, g: int = 0, b: int = 0, upper: bool = False, add_hashtag: bool = True) -> str:
    if (not isinstance(r, Number) or not isinstance(g, Number) or not isinstance(b, Number)):
        raise (TypeError())
    
    result = '#' if add_hashtag else ''
    result += hex(r).replace('0x', '').zfill(2)
    result += hex(g).replace('0x', '').zfill(2)
    result += hex(b).replace('0x', '').zfill(2)

    return (result.upper() if upper else result)

def rgba_to_hex(r: int = 0, g: int = 0, b: int = 0, a: int = 0, upper: bool = False, add_hashtag: bool = True) -> str:
    if (not isinstance(r, Number) or not isinstance(g, Number) or not isinstance(b, Number) or not isinstance(a, Number)):
        raise (TypeError())
    
    result = '#' if add_hashtag else ''
    result += hex(r).replace('0x', '').zfill(2)
    result += hex(g).replace('0x', '').zfill(2)
    result += hex(b).replace('0x', '').zfill(2)
    result += hex(a).replace('0x', '').zfill(2)

    return (result.upper() if upper else result)

def rgb_to_endian(r: int = 0, g: int = 0, b: int = 0) -> int:
    if (not isinstance(r, Number) or not isinstance(g, Number) or not isinstance(b, Number)):
        raise (TypeError())

    return ((((r << 8) + g) << 8) + b)

def rgba_to_endian(r: int = 0, g: int = 0, b: int = 0, a: int = 0) -> int:
    if (not isinstance(r, Number) or not isinstance(g, Number) or not isinstance(b, Number) or not isinstance(a, Number)):
        raise (TypeError())

    return ((((((r << 8) + g) << 8) + b) << 8) + a)

def endian_to_rgb(color: int) -> tuple:
    if (not isinstance(color, Number)):
        raise (TypeError())

    red: int = (color >> 16)
    green: int = (color >> 8) & 0xFF
    blue: int = color & 0xFF

    return (red, green, blue)

def endian_to_rgba(color: int) -> tuple:
    if (not isinstance(color, Number)):
        raise (TypeError())

    red: int = (color >> 24)
    green: int = (color >> 16) & 0xFF
    blue: int = (color >> 8) & 0xFF
    alpha: int = color & 0xFF

    return (red, green, blue, alpha)
