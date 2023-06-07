from typing import Callable

def pattern_heart_empty(size: int, sep: str = '', end: str = '\n', char: str = '*', empty_char: str = ' ') -> str:
    get_top: Callable = lambda i: ''.join((char + sep if (j == 1 or j == i or i == size // 2) else " " + sep) for j in range(1, i + 1, 1))
    top: tuple = tuple((((empty_char + sep) * ((size - i) // 2)) + get_top(i) + ((empty_char + sep) * (size - i)) + get_top(i)) for i in range(size // 2, size, 2))
    bottom: tuple = tuple((((empty_char + sep) * (size - i)) + ''.join(char + sep if (j == 1 or j == i * 2 - 1 or (i == size and j == i)) else empty_char + sep for j in range(1, i * 2, 1))) for i in range(size, 0, -1))

    return (end.join((*top, *bottom)))

def pattern_heart_fill(size: int, sep: str = '', end: str = '\n', char: str = '*', empty_char: str = ' ') -> str:
    top: tuple = tuple((((empty_char + sep) * ((size - i) // 2)) + ((char + sep) * i) + ((empty_char + sep) * (size - i)) + ((char + sep) * i)) for i in range(size // 2, size, 2))
    bottom: tuple = tuple((((empty_char + sep) * (size - i)) + ((char + sep) * (i * 2 - 1))) for i in range(size, 0, -1))

    return (end.join((*top, *bottom)))

def pattern_square_fill(size: int, sep: str = '', end: str = '\n', char: str = '*', empty_char: str = ' ') -> str:
    return (end.join((char + sep) * size for _ in range(size)))

def pattern_square_empty(size: int, sep: str = '', end: str = '\n', char: str = '*', empty_char: str = ' ') -> str:
    return (end.join((((char + sep) * size if i == 0 or i == size - 1 else (char + sep) + ((empty_char + sep) * (size - 2)) + (char + sep))) for i in range(size)))

def pattern_rectangle_fill(width: int, height: int, sep: str = '', end: str = '\n', char: str = '*', empty_char: str = ' ') -> str:
    return (end.join((char + sep) * width for _ in range(height)))

def pattern_rectangle_empty(width: int, height: int, sep: str = '', end: str = '\n', char: str = '*', empty_char: str = ' ') -> str:
    return (end.join((((char + sep) * width if i == 0 or i == height - 1 else (char + sep) + ((empty_char + sep) * (width - 2)) + (char + sep))) for i in range(height)))

def pattern_triangle_fill(size: int, sep: str = '', end: str = '\n', char: str = '*', empty_char: str = ' ') -> str:
    return (end.join((char + sep) * i for i in range(size + 1)))

def pattern_triangle_empty(size: int, sep: str = '', end: str = '\n', char: str = '*', empty_char: str = ' ') -> str:
    return (end.join((((char + sep) * (i + 1) if i == 0 or i == size - 1 else (char + sep) + ((empty_char + sep) * (i + 1 - 2)) + (char + sep))) for i in range(size)))

def pattern_pyramid_fill(size: int, sep: str = '', end: str = '\n', char: str = '*', empty_char: str = ' ') -> str:
    return (end.join(empty_char * (size - i) + (char + sep) * i for i in range(size + 1)))

def pattern_pyramid_empty(size: int, sep: str = '', end: str = '\n', char: str = '*', empty_char: str = ' ') -> str:
    return (end.join(((empty_char * (size - i) + ((char + sep) * (i + 1) if i == 0 or i == size - 1 else (char + sep) + ((empty_char + sep) * (i + 1 - 2)) + (char + sep)))) for i in range(size)))

def pattern_upside_pyramid_fill(size: int, sep: str = '', end: str = '\n', char: str = '*', empty_char: str = ' ') -> str:
    return (end.join(empty_char * (size - i) + (char + sep) * i for i in range(size, 0, -1)))

def pattern_upside_pyramid_empty(size: int, sep: str = '', end: str = '\n', char: str = '*', empty_char: str = ' ') -> str:
    return (end.join(((empty_char * (size - i) + ((char + sep) * (i + 1) if i == 0 or i == size - 1 else (char + sep) + ((empty_char + sep) * (i + 1 - 2)) + (char + sep)))) for i in range(size - 1, -1, -1)))
