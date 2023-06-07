import builtins

from .list_prototype import (
    round_list,
    div_list,
    mod_list,
    mul_list,
    sub_list,
    sum_list,
    div_floor_list,
    PrototypedList
)

def init_prototypes() -> None:
    builtins.list = PrototypedList
