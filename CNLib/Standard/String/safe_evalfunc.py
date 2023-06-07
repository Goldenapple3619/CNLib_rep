from typing import Any, Mapping

_ALLOWED_FUNCTIONS = [
    "sin",
    "cos",
    "tan",
    "sinh",
    "cosh",
    "tanh",
    "acos",
    "atan",
    "asin",
    "asinh",
    "atanh",
    "acosh",
    "log10",
    "log2",
    "log",
    "exp",
    "+",
    "-",
    "*",
    "/",
    "%",
    ".",
    "(",
    ")",
    " "
]

def safe_eval(__source: str, __globals: dict = None, __locals: Mapping = None) -> Any:
    if (not isinstance(__source, str)):
        raise TypeError()

    check: str = __source

    for item in _ALLOWED_FUNCTIONS:
        check = check.replace(item, "")

    if (not check.isnumeric()):
        return (None)

    return (eval(__source, __globals, __locals))
