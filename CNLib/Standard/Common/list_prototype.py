from typing import Callable
from re import match

def round_list(__obj: list, __ndigit: int = None) -> None:
    for i, item in enumerate(__obj):
        __obj[i] = round(item, __ndigit)

def sum_list(__obj: list, returned_obj: Callable = int) -> int:
    result: returned_obj = returned_obj()

    for item in __obj:
        result += item
    return (result)

def sub_list(__obj: list, returned_obj: Callable = int) -> int:
    result: returned_obj = returned_obj()

    for item in __obj:
        result -= item
    return (result)

def div_list(__obj: list, returned_obj: Callable = int) -> int:
    result: returned_obj = returned_obj()

    for item in __obj:
        result /= item
    return (result)

def div_floor_list(__obj: list, returned_obj: Callable = int) -> int:
    result: returned_obj = returned_obj()

    for item in __obj:
        result //= item
    return (result)

def mul_list(__obj: list, returned_obj: Callable = int) -> int:
    result: returned_obj = returned_obj()

    for item in __obj:
        result *= item
    return (result)

def mod_list(__obj: list, returned_obj: Callable = int) -> int:
    result: returned_obj = returned_obj()

    for item in __obj:
        result %= item
    return (result)

def exclude_list(__obj: list, pattern: str) -> None:
    shift: int = 0

    for i, item in enumerate(__obj.copy()):
        if (not match(pattern, str(item))):
            __obj.pop(i - shift)
            shift += 1

class PrototypedList(list):
    round = round_list
    __round__ = round_list

    sum = sum_list
    sub = sub_list
    mul = mul_list
    div = div_list
    floor_div = div_floor_list
    mod = mod_list
    exclude = exclude_list
