from .getch import *

def _str_to_ascii(text: str) -> int:
    return (int.from_bytes(text, 'little'))

def custom_input(display: str = '') -> str:
    pressed: bytes = b'0'
    text: str = ''

    print(display, end='', flush=True)
    while (_str_to_ascii(pressed) not in (13, 10)):
        pressed: bytes = getch()

        if (_str_to_ascii(pressed) in (8, 127)):
            text = text[:-1]
            print("\b \b", end='', flush=True)
        elif (_str_to_ascii(pressed) in (13, 10)):
            continue
        elif (_str_to_ascii(pressed) in (0, 3)):
            getch()
            continue
        elif (_str_to_ascii(pressed) == 27):
            getch()
            getch()
            continue
        elif (pressed.isascii()):
            text += pressed.decode()
            print(pressed.decode(), end='', flush=True)
    print('\n', end = '')

    return (text)

def replaced_input(display: str = '', char: str = '*') -> str:
    pressed: bytes = b'0'
    text: str = ''

    print(display, end='', flush=True)
    while (_str_to_ascii(pressed) not in (13, 10)):
        pressed: bytes = getch()

        if (_str_to_ascii(pressed) in (8, 127)):
            text = text[:-1]
            print("\b \b", end='', flush=True)
        elif (_str_to_ascii(pressed) in (13, 10)):
            continue
        elif (_str_to_ascii(pressed) in (0, 3)):
            getch()
            continue
        elif (_str_to_ascii(pressed) == 27):
            getch()
            getch()
            continue
        elif (pressed.isascii()):
            text += pressed.decode()
            print(char, end='', flush=True)
    print('\n', end = '')

    return (text)
