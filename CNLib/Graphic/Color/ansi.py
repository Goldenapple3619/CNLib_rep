ESCAPE_CHAR: str = '\x1B'

def code_fore_from_rgb(r: int, g: int, b: int) -> str:
    return (f'{ESCAPE_CHAR}[38;2;{r};{g};{b}m')

def code_back_from_rgb(r: int, g: int, b: int) -> str:
    return (f'{ESCAPE_CHAR}[48;2;{r};{g};{b}m')

def code_fore_system(color: int) -> str:
    return (f'{ESCAPE_CHAR}[{30 + color}m')

def code_back_system(color: int) -> str:
    return (f'{ESCAPE_CHAR}[{40 + color}m')

def code_fore_256(color: int) -> str:
    return (f'{ESCAPE_CHAR}[38;5;{color}m')

def code_back_256(color: int) -> str:
    return (f'{ESCAPE_CHAR}[48;5;{color}m')

def code_reset() -> str:
    return (f'{ESCAPE_CHAR}[0m')

def code_bold() -> str:
    return (f'{ESCAPE_CHAR}[1m')

def code_faint() -> str:
    return (f'{ESCAPE_CHAR}[2m')

def code_italic() -> str:
    return (f'{ESCAPE_CHAR}[3m')

def code_underline() -> str:
    return (f'{ESCAPE_CHAR}[4m')

def code_blinking() -> str:
    return (f'{ESCAPE_CHAR}[5m')

def code_inverse() -> str:
    return (f'{ESCAPE_CHAR}[7m')

def code_hidden() -> str:
    return (f'{ESCAPE_CHAR}[8m')

def code_strikethrough() -> str:
    return (f'{ESCAPE_CHAR}[9m')

def code_invisible_cursor() -> str:
    return (f'{ESCAPE_CHAR}[?25l')

def code_visible_cursor() -> str:
    return (f'{ESCAPE_CHAR}[?25h')
