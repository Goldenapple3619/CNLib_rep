from CNLib.Graphic import *

from .test_const import *


"""
hex_to_rgb testing
"""

@tests(name = "color_hex_to_rgb")
def test():
    return (hex_to_rgb("#ffffff") == (255, 255, 255))

@tests(name = "color_hex_to_rgb_unfill")
def test():
    return (hex_to_rgb("#ffff") == (255, 255, 0))

@tests(name = "color_hex_to_rgb_little_number")
def test():
    return (hex_to_rgb("#050001") == (5, 0, 1))

@tests(name = "color_hex_to_rgb_no_hashtag")
def test():
    return (hex_to_rgb("050001") == (5, 0, 1))

@tests(name = "color_hex_to_rgb_empty")
def test():
    return (hex_to_rgb("") == (0, 0, 0))

@tests(name = "color_hex_to_rgb_too_big")
def test():
    try:
        hex_to_rgb("ffffffff")
        return (0)
    except ValueError:
        return (1)

@tests(name = "color_hex_to_rgb_invalid_char")
def test():
    try:
        hex_to_rgb("abcdp")
        return (0)
    except BaseException:
        return (1)

@tests(name = "color_hex_to_rgb_no_string")
def test():
    try:
        hex_to_rgb(5)
        return (0)
    except TypeError:
        return (1)


"""
hex_to_rgba testing
"""

@tests(name = "color_hex_to_rgba")
def test():
    return (hex_to_rgba("#ffffffff") == (255, 255, 255, 255))

@tests(name = "color_hex_to_rgba_unfill")
def test():
    return (hex_to_rgba("#ffffff") == (255, 255, 255, 0))

@tests(name = "color_hex_to_rgba_little_number")
def test():
    return (hex_to_rgba("#05000100") == (5, 0, 1, 0))

@tests(name = "color_hex_to_rgba_no_hashtag")
def test():
    return (hex_to_rgba("05000100") == (5, 0, 1, 0))

@tests(name = "color_hex_to_rgba_empty")
def test():
    return (hex_to_rgba("") == (0, 0, 0, 0))

@tests(name = "color_hex_to_rgba_too_big")
def test():
    try:
        hex_to_rgba("ffffffffff")
        return (0)
    except ValueError:
        return (1)

@tests(name = "color_hex_to_rgba_invalid_char")
def test():
    try:
        hex_to_rgba("abcdp")
        return (0)
    except BaseException:
        return (1)

@tests(name = "color_hex_to_rgba_no_string")
def test():
    try:
        hex_to_rgba(5)
        return (0)
    except TypeError:
        return (1)


"""
rgb_to_hex testing
"""

@tests(name = "color_rgb_to_hex")
def test():
    return (rgb_to_hex(255, 255, 255) == "#ffffff")

@tests(name = "color_rgb_to_hex_no_hashtag")
def test():
    return (rgb_to_hex(255, 255, 255, add_hashtag=False) == "ffffff")

@tests(name = "color_rgb_to_hex_no_arg")
def test():
    return (rgb_to_hex() == "#000000")

@tests(name = "color_rgb_to_hex_little_number")
def test():
    return (rgb_to_hex(1, 0, 5) == "#010005")

@tests(name = "color_rgb_to_hex_upper")
def test():
    return (rgb_to_hex(255, 255, 255, True) == "#FFFFFF")

@tests(name = "color_rgb_to_hex_invalid_arg")
def test():
    try:
        rgb_to_hex(255, 255, "a")
        return (0)
    except TypeError:
        return (1)


"""
rgba_to_hex testing
"""

@tests(name = "color_rgba_to_hex")
def test():
    return (rgba_to_hex(255, 255, 255, 255) == "#ffffffff")

@tests(name = "color_rgba_to_hex_no_hashtag")
def test():
    return (rgba_to_hex(255, 255, 255, 255, add_hashtag=False) == "ffffffff")

@tests(name = "color_rgba_to_hex_no_arg")
def test():
    return (rgba_to_hex() == "#00000000")

@tests(name = "color_rgba_to_hex_little_number")
def test():
    return (rgba_to_hex(1, 0, 5, 2) == "#01000502")

@tests(name = "color_rgba_to_hex_upper")
def test():
    return (rgba_to_hex(255, 255, 255, 255, True) == "#FFFFFFFF")

@tests(name = "color_rgba_to_hex_invalid_arg")
def test():
    try:
        rgba_to_hex(255, 255, 255, "a")
        return (0)
    except TypeError:
        return (1)


"""
endian_conversion_rgb testing
"""

@tests(name = "color_endian_conversion_rgb", args=((255, 255, 255),))
def test(color: tuple):
    return (endian_to_rgb(rgb_to_endian(*color)) == color)

@tests(name = "color_endian_conversion_rgb_null")
def test():
    return (endian_to_rgb(rgb_to_endian()) == (0, 0, 0))

@tests(name = "color_endian_conversion_rgb_little", args=((2, 5, 6),))
def test(color: tuple):
    return (endian_to_rgb(rgb_to_endian(*color)) == color)

@tests(name = "color_endian_conversion_rgb_invalid_arg", args=((255, 'a', 255),))
def test(color: tuple):
    try:
        endian_to_rgb(rgb_to_endian(*color))
        return (0)
    except TypeError:
        return (1)


"""
endian_conversion_rgba testing
"""

@tests(name = "color_endian_conversion_rgba", args=((255, 255, 255, 255),))
def test(color: tuple):
    return (endian_to_rgba(rgba_to_endian(*color)) == color)

@tests(name = "color_endian_conversion_rgba_null")
def test():
    return (endian_to_rgba(rgba_to_endian()) == (0, 0, 0, 0))

@tests(name = "color_endian_conversion_rgba_little", args=((2, 5, 6, 3),))
def test(color: tuple):
    return (endian_to_rgba(rgba_to_endian(*color)) == color)

@tests(name = "color_endian_conversion_rgba_invalid_arg", args=((255, 'a', 255, 255),))
def test(color: tuple):
    try:
        endian_to_rgba(rgba_to_endian(*color))
        return (0)
    except TypeError:
        return (1)


"""
ansi_code testing
"""

@tests(name = "ansi_code_reset")
def test():
    return (code_reset() == "\x1B[0m")

@tests(name = "ansi_code_bold")
def test():
    return (code_bold() == "\x1B[1m")

@tests(name = "ansi_code_faint")
def test():
    return (code_faint() == "\x1B[2m")

@tests(name = "ansi_code_italic")
def test():
    return (code_italic() == "\x1B[3m")

@tests(name = "ansi_code_underline")
def test():
    return (code_underline() == "\x1B[4m")

@tests(name = "ansi_code_blinking")
def test():
    return (code_blinking() == "\x1B[5m")

@tests(name = "ansi_code_inverse")
def test():
    return (code_inverse() == "\x1B[7m")

@tests(name = "ansi_code_hidden")
def test():
    return (code_hidden() == "\x1B[8m")

@tests(name = "ansi_code_strikethrough")
def test():
    return (code_strikethrough() == "\x1B[9m")

@tests(name = "ansi_code_invisible_cursor")
def test():
    return (code_invisible_cursor() == "\x1B[?25l")

@tests(name = "ansi_code_visible_cursor")
def test():
    return (code_visible_cursor() == "\x1B[?25h")

@tests(name = "ansi_code_back256")
def test():
    return (code_back_256(6) == "\x1B[48;5;6m")

@tests(name = "ansi_code_fore256")
def test():
    return (code_fore_256(15) == "\x1B[38;5;15m")

@tests(name = "ansi_code_fore_system")
def test():
    return (code_fore_system(7) == "\x1B[37m")

@tests(name = "ansi_code_back_system")
def test():
    return (code_back_system(3) == "\x1B[43m")

@tests(name = "ansi_code_back_from_rgb")
def test():
    return (code_back_from_rgb(255, 3, 12) == "\x1B[48;2;255;3;12m")

@tests(name = "ansi_code_fore_from_rgb")
def test():
    return (code_fore_from_rgb(4, 55, 125) == "\x1B[38;2;4;55;125m")
