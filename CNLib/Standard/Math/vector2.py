from numbers import Number
from typing import Iterable
from math import sqrt

class Vector2(object):
    def __init__(self, x: Number, y: Number) -> None:
        self.x = x
        self.y = y

    def copy(self) -> object:
        return (Vector2(self.x, self.y))
    
    def clear(self) -> None:
        self.x = 0
        self.y = 0

    def reverse(self) -> None:
        self.x, self.y = self.y, self.x

    def __repr__(self) -> str:
        return (f"({self.x}, {self.y})")
    
    def __str__(self) -> str:
        return (f"({self.x}, {self.y})")
    
    def __mul__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector2(self.x * __other, self.y * __other))
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (Vector2(self.x * __other.x, self.y * __other.y))
        if (hasattr(__other, "x")):
            return (Vector2(self.x * __other.x, self.y * __other.x))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector2(self.x, self.y))
            if (len(__other == 1)):
                return (Vector2(self.x * __other[0], self.y * __other[0]))
            if (len(__other > 1)):
                return (Vector2(self.x * __other[0], self.y * __other[1]))
            
    def __add__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector2(self.x + __other, self.y + __other))
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (Vector2(self.x + __other.x, self.y + __other.y))
        if (hasattr(__other, "x")):
            return (Vector2(self.x + __other.x, self.y + __other.x))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector2(self.x, self.y))
            if (len(__other == 1)):
                return (Vector2(self.x + __other[0], self.y + __other[0]))
            if (len(__other > 1)):
                return (Vector2(self.x + __other[0], self.y + __other[1]))

    def __sub__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector2(self.x - __other, self.y - __other))
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (Vector2(self.x - __other.x, self.y - __other.y))
        if (hasattr(__other, "x")):
            return (Vector2(self.x - __other.x, self.y - __other.x))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector2(self.x, self.y))
            if (len(__other == 1)):
                return (Vector2(self.x - __other[0], self.y - __other[0]))
            if (len(__other > 1)):
                return (Vector2(self.x - __other[0], self.y - __other[1]))
            
    def __truediv__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector2(self.x / __other, self.y / __other))
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (Vector2(self.x / __other.x, self.y / __other.y))
        if (hasattr(__other, "x")):
            return (Vector2(self.x / __other.x, self.y / __other.x))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector2(self.x, self.y))
            if (len(__other == 1)):
                return (Vector2(self.x / __other[0], self.y / __other[0]))
            if (len(__other > 1)):
                return (Vector2(self.x / __other[0], self.y / __other[1]))
            
    def __floordiv__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector2(self.x // __other, self.y // __other))
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (Vector2(self.x // __other.x, self.y // __other.y))
        if (hasattr(__other, "x")):
            return (Vector2(self.x // __other.x, self.y // __other.x))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector2(self.x, self.y))
            if (len(__other == 1)):
                return (Vector2(self.x // __other[0], self.y // __other[0]))
            if (len(__other > 1)):
                return (Vector2(self.x // __other[0], self.y // __other[1]))

    def __pow__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector2(self.x ** __other, self.y ** __other))
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (Vector2(self.x ** __other.x, self.y ** __other.y))
        if (hasattr(__other, "x")):
            return (Vector2(self.x ** __other.x, self.y ** __other.x))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector2(self.x, self.y))
            if (len(__other == 1)):
                return (Vector2(self.x ** __other[0], self.y ** __other[0]))
            if (len(__other > 1)):
                return (Vector2(self.x ** __other[0], self.y ** __other[1]))
            
    def __mod__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector2(self.x % __other, self.y % __other))
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (Vector2(self.x % __other.x, self.y % __other.y))
        if (hasattr(__other, "x")):
            return (Vector2(self.x % __other.x, self.y % __other.x))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector2(self.x, self.y))
            if (len(__other == 1)):
                return (Vector2(self.x % __other[0], self.y % __other[0]))
            if (len(__other > 1)):
                return (Vector2(self.x % __other[0], self.y % __other[1]))
            
    def __matmul__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector2(self.x @ __other, self.y @ __other))
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (Vector2(self.x @ __other.x, self.y @ __other.y))
        if (hasattr(__other, "x")):
            return (Vector2(self.x @ __other.x, self.y @ __other.x))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector2(self.x, self.y))
            if (len(__other == 1)):
                return (Vector2(self.x @ __other[0], self.y @ __other[0]))
            if (len(__other > 1)):
                return (Vector2(self.x @ __other[0], self.y @ __other[1]))
            
    def __and__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector2(self.x & __other, self.y & __other))
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (Vector2(self.x & __other.x, self.y & __other.y))
        if (hasattr(__other, "x")):
            return (Vector2(self.x & __other.x, self.y & __other.x))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector2(self.x, self.y))
            if (len(__other == 1)):
                return (Vector2(self.x & __other[0], self.y & __other[0]))
            if (len(__other > 1)):
                return (Vector2(self.x & __other[0], self.y & __other[1]))
            
    def __or__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector2(self.x | __other, self.y | __other))
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (Vector2(self.x | __other.x, self.y | __other.y))
        if (hasattr(__other, "x")):
            return (Vector2(self.x | __other.x, self.y | __other.x))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector2(self.x, self.y))
            if (len(__other == 1)):
                return (Vector2(self.x | __other[0], self.y | __other[0]))
            if (len(__other > 1)):
                return (Vector2(self.x | __other[0], self.y | __other[1]))
            
    def __xor__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector2(self.x ^ __other, self.y ^ __other))
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (Vector2(self.x ^ __other.x, self.y ^ __other.y))
        if (hasattr(__other, "x")):
            return (Vector2(self.x ^ __other.x, self.y ^ __other.x))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector2(self.x, self.y))
            if (len(__other == 1)):
                return (Vector2(self.x ^ __other[0], self.y ^ __other[0]))
            if (len(__other > 1)):
                return (Vector2(self.x ^ __other[0], self.y ^ __other[1]))

    def __lshift__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector2(self.x << __other, self.y << __other))
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (Vector2(self.x << __other.x, self.y << __other.y))
        if (hasattr(__other, "x")):
            return (Vector2(self.x << __other.x, self.y << __other.x))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector2(self.x, self.y))
            if (len(__other == 1)):
                return (Vector2(self.x << __other[0], self.y << __other[0]))
            if (len(__other > 1)):
                return (Vector2(self.x << __other[0], self.y << __other[1]))
            
    def __rshift__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector2(self.x >> __other, self.y >> __other))
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (Vector2(self.x >> __other.x, self.y >> __other.y))
        if (hasattr(__other, "x")):
            return (Vector2(self.x >> __other.x, self.y >> __other.x))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector2(self.x, self.y))
            if (len(__other == 1)):
                return (Vector2(self.x >> __other[0], self.y >> __other[0]))
            if (len(__other > 1)):
                return (Vector2(self.x >> __other[0], self.y >> __other[1]))

    def __neg__(self) -> object:
        return (Vector2(-self.x, -self.y))
    
    def __pos__(self) -> object:
        return (Vector2(+self.x, +self.y))
    
    def __abs__(self) -> object:
        return (Vector2(abs(self.x), abs(self.y)))
    
    def __invert__(self) -> object:
        return (Vector2(~self.x, ~self.y))
    
    def __round__(self, __ndigit: int = None) -> object:
        return (Vector2(round(self.x, __ndigit), round(self.y, __ndigit)))
    
    def __hash__(self) -> int:
        return (hash(self))

    def __len__(self) -> int:
        return (2)
    
    def __getitem__(self, __key: int) -> int:
        if (__key > 1 or __key < -2):
            raise IndexError
        if (__key == 0 or __key == -2):
            return (self.x)
        if (__key == 1 or __key == -1):
            return (self.y)

    def __setitem__(self, __key: int, __value: int):
        if (__key > 1 or __key < -2):
            raise IndexError
        if (__key == 0 or __key == -2):
            self.x = __value
        if (__key == 1 or __key == -1):
            self.y = __value

    def __delitem__(self, __key: int) -> int:
        if (__key > 1 or __key < -2):
            raise IndexError
        if (__key == 0 or __key == -2):
            self.x = 0
        if (__key == 1 or __key == -1):
            self.y = 0

    def __reversed__(self) -> object:
        return (Vector2(self.y, self.x))
    
    def __contains__(self, __item) -> bool:
        return (True if __item == self.x or __item == self.y else False)
    
    def __eq__(self, __other: object) -> bool:
        if (isinstance(__other, Number)):
            return (self.x == __other and self.y == __other)
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (self.x == __other.x and self.y == __other.y)
        if (hasattr(__other, "x")):
            return (self.x == __other.x and self.y == __other.x)
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (self.x == 0 and self.y == 0)
            if (len(__other == 1)):
                return (self.x == __other[0] and self.y == __other[0])
            if (len(__other > 1)):
                return (self.x == __other[0] and self.y == __other[1])
            
    def __ne__(self, __other: object) -> bool:
        if (isinstance(__other, Number)):
            return (self.x != __other and self.y != __other)
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (self.x != __other.x and self.y != __other.y)
        if (hasattr(__other, "x")):
            return (self.x != __other.x and self.y != __other.x)
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (self.x != 0 and self.y != 0)
            if (len(__other == 1)):
                return (self.x != __other[0] and self.y != __other[0])
            if (len(__other > 1)):
                return (self.x != __other[0] and self.y != __other[1])
            
    def __lt__(self, __other: object) -> bool:
        if (isinstance(__other, Number)):
            return (self.x < __other and self.y < __other)
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (self.x < __other.x and self.y < __other.y)
        if (hasattr(__other, "x")):
            return (self.x < __other.x and self.y < __other.x)
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (self.x < 0 and self.y < 0)
            if (len(__other == 1)):
                return (self.x < __other[0] and self.y < __other[0])
            if (len(__other > 1)):
                return (self.x < __other[0] and self.y < __other[1])
            
    def __le__(self, __other: object) -> bool:
        if (isinstance(__other, Number)):
            return (self.x <= __other and self.y <= __other)
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (self.x <= __other.x and self.y <= __other.y)
        if (hasattr(__other, "x")):
            return (self.x <= __other.x and self.y <= __other.x)
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (self.x <= 0 and self.y <= 0)
            if (len(__other == 1)):
                return (self.x <= __other[0] and self.y <= __other[0])
            if (len(__other > 1)):
                return (self.x <= __other[0] and self.y <= __other[1])
            
    def __gt__(self, __other: object) -> bool:
        if (isinstance(__other, Number)):
            return (self.x > __other and self.y > __other)
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (self.x > __other.x and self.y > __other.y)
        if (hasattr(__other, "x")):
            return (self.x > __other.x and self.y > __other.x)
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (self.x > 0 and self.y > 0)
            if (len(__other == 1)):
                return (self.x > __other[0] and self.y > __other[0])
            if (len(__other > 1)):
                return (self.x > __other[0] and self.y > __other[1])
            
    def __ge__(self, __other: object) -> bool:
        if (isinstance(__other, Number)):
            return (self.x >= __other and self.y >= __other)
        if (hasattr(__other, "x") and hasattr(__other, "y")):
            return (self.x >= __other.x and self.y >= __other.y)
        if (hasattr(__other, "x")):
            return (self.x >= __other.x and self.y >= __other.x)
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (self.x >= 0 and self.y >= 0)
            if (len(__other == 1)):
                return (self.x >= __other[0] and self.y >= __other[0])
            if (len(__other > 1)):
                return (self.x >= __other[0] and self.y >= __other[1])
            
    def to_list(self) -> list:
        return [self.x, self.y]

def vector2_distance(__vec: Vector2, __second_vec: Vector2) -> float:
    return (
        sqrt(
            pow(__second_vec.x - __vec.x, 2) +
            pow(__second_vec.y - __vec.y, 2)
        )
    )

def vector3_form_pos(pos_origin: Vector2, pos_end: Vector2) -> Vector2:
    return (Vector2(
        pos_end.x - pos_origin.x,
        pos_end.y - pos_origin.y
    ))
