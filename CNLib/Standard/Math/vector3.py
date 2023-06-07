from numbers import Number
from typing import Iterable
from math import sqrt

class Vector3(object):
    def __init__(self, x: Number, y: Number, z: Number) -> None:
        self.x = x
        self.y = y
        self.z = z

    def copy(self) -> object:
        return (Vector3(self.x, self.y, self.z))
    
    def clear(self) -> None:
        self.x = 0
        self.y = 0
        self.z = 0

    def reverse(self) -> None:
        self.x, self.z = self.z, self.x

    def __repr__(self) -> str:
        return (f"({self.x}, {self.y}, {self.z})")
    
    def __str__(self) -> str:
        return (f"({self.x}, {self.y}, {self.z})")
    
    def __mul__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector3(self.x * __other, self.y * __other, self.z * __other))
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (Vector3(self.x * __other.x, self.y * __other.y, self.z * __other.z))
        if (hasattr(__other, "x")):
            return (Vector3(self.x * __other.x, self.y * __other.x, self.z * __other.z))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector3(self.x, self.y, self.z))
            if (len(__other == 1)):
                return (Vector3(self.x * __other[0], self.y * __other[0], self.z * __other[0]))
            if (len(__other > 2)):
                return (Vector3(self.x * __other[0], self.y * __other[1], self.z * __other[2]))
            
    def __add__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector3(self.x + __other, self.y + __other, self.z + __other))
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (Vector3(self.x + __other.x, self.y + __other.y, self.z + __other.z))
        if (hasattr(__other, "x")):
            return (Vector3(self.x + __other.x, self.y + __other.x, self.z + __other.z))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector3(self.x, self.y, self.z))
            if (len(__other == 1)):
                return (Vector3(self.x + __other[0], self.y + __other[0], self.z + __other[0]))
            if (len(__other > 2)):
                return (Vector3(self.x + __other[0], self.y + __other[1], self.z + __other[2]))

    def __sub__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector3(self.x - __other, self.y - __other, self.z - __other))
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (Vector3(self.x - __other.x, self.y - __other.y, self.z - __other.z))
        if (hasattr(__other, "x")):
            return (Vector3(self.x - __other.x, self.y - __other.x, self.z - __other.z))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector3(self.x, self.y, self.z))
            if (len(__other == 1)):
                return (Vector3(self.x - __other[0], self.y - __other[0], self.z - __other[0]))
            if (len(__other > 2)):
                return (Vector3(self.x - __other[0], self.y - __other[1], self.z - __other[2]))
            
    def __truediv__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector3(self.x / __other, self.y / __other, self.z / __other))
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (Vector3(self.x / __other.x, self.y / __other.y, self.z / __other.z))
        if (hasattr(__other, "x")):
            return (Vector3(self.x / __other.x, self.y / __other.x, self.z / __other.z))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector3(self.x, self.y, self.z))
            if (len(__other == 1)):
                return (Vector3(self.x / __other[0], self.y / __other[0], self.z / __other[0]))
            if (len(__other > 2)):
                return (Vector3(self.x / __other[0], self.y / __other[1], self.z / __other[2]))
            
    def __floordiv__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector3(self.x // __other, self.y // __other, self.z // __other))
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (Vector3(self.x // __other.x, self.y // __other.y, self.z // __other.z))
        if (hasattr(__other, "x")):
            return (Vector3(self.x // __other.x, self.y // __other.x, self.z // __other.z))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector3(self.x, self.y, self.z))
            if (len(__other == 1)):
                return (Vector3(self.x // __other[0], self.y // __other[0], self.z // __other[0]))
            if (len(__other > 2)):
                return (Vector3(self.x // __other[0], self.y // __other[1], self.z // __other[2]))

    def __pow__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector3(self.x ** __other, self.y ** __other, self.z ** __other))
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (Vector3(self.x ** __other.x, self.y ** __other.y, self.z ** __other.z))
        if (hasattr(__other, "x")):
            return (Vector3(self.x ** __other.x, self.y ** __other.x, self.z ** __other.z))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector3(self.x, self.y, self.z))
            if (len(__other == 1)):
                return (Vector3(self.x ** __other[0], self.y ** __other[0], self.z ** __other[0]))
            if (len(__other > 2)):
                return (Vector3(self.x ** __other[0], self.y ** __other[1], self.z ** __other[2]))
            
    def __mod__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector3(self.x % __other, self.y % __other, self.z % __other))
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (Vector3(self.x % __other.x, self.y % __other.y, self.z % __other.z))
        if (hasattr(__other, "x")):
            return (Vector3(self.x % __other.x, self.y % __other.x, self.z % __other.z))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector3(self.x, self.y, self.z))
            if (len(__other == 1)):
                return (Vector3(self.x % __other[0], self.y % __other[0], self.z % __other[0]))
            if (len(__other > 2)):
                return (Vector3(self.x % __other[0], self.y % __other[1], self.z % __other[2]))
            
    def __matmul__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector3(self.x @ __other, self.y @ __other, self.z @ __other))
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (Vector3(self.x @ __other.x, self.y @ __other.y, self.z @ __other.z))
        if (hasattr(__other, "x")):
            return (Vector3(self.x @ __other.x, self.y @ __other.x, self.z @ __other.z))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector3(self.x, self.y, self.z))
            if (len(__other == 1)):
                return (Vector3(self.x @ __other[0], self.y @ __other[0], self.z @ __other[0]))
            if (len(__other > 2)):
                return (Vector3(self.x @ __other[0], self.y @ __other[1], self.z @ __other[2]))
            
    def __and__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector3(self.x & __other, self.y & __other, self.z & __other))
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (Vector3(self.x & __other.x, self.y & __other.y, self.z & __other.z))
        if (hasattr(__other, "x")):
            return (Vector3(self.x & __other.x, self.y & __other.x, self.z & __other.z))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector3(self.x, self.y, self.z))
            if (len(__other == 1)):
                return (Vector3(self.x & __other[0], self.y & __other[0], self.z & __other[0]))
            if (len(__other > 2)):
                return (Vector3(self.x & __other[0], self.y & __other[1], self.z & __other[2]))
            
    def __or__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector3(self.x | __other, self.y | __other, self.z | __other))
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (Vector3(self.x | __other.x, self.y | __other.y, self.z | __other.z))
        if (hasattr(__other, "x")):
            return (Vector3(self.x | __other.x, self.y | __other.x, self.z | __other.z))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector3(self.x, self.y, self.z))
            if (len(__other == 1)):
                return (Vector3(self.x | __other[0], self.y | __other[0], self.z | __other[0]))
            if (len(__other > 2)):
                return (Vector3(self.x | __other[0], self.y | __other[1], self.z | __other[2]))
            
    def __xor__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector3(self.x ^ __other, self.y ^ __other, self.z ^ __other))
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (Vector3(self.x ^ __other.x, self.y ^ __other.y, self.z ^ __other.z))
        if (hasattr(__other, "x")):
            return (Vector3(self.x ^ __other.x, self.y ^ __other.x, self.z ^ __other.z))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector3(self.x, self.y, self.z))
            if (len(__other == 1)):
                return (Vector3(self.x ^ __other[0], self.y ^ __other[0], self.z ^ __other[0]))
            if (len(__other > 2)):
                return (Vector3(self.x ^ __other[0], self.y ^ __other[1], self.z ^ __other[2]))

    def __lshift__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector3(self.x << __other, self.y << __other, self.z << __other))
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (Vector3(self.x << __other.x, self.y << __other.y, self.z << __other.z))
        if (hasattr(__other, "x")):
            return (Vector3(self.x << __other.x, self.y << __other.x, self.z << __other.z))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector3(self.x, self.y, self.z))
            if (len(__other == 1)):
                return (Vector3(self.x << __other[0], self.y << __other[0], self.z << __other[0]))
            if (len(__other > 2)):
                return (Vector3(self.x << __other[0], self.y << __other[1], self.z << __other[2]))
            
    def __rshift__(self, __other: object) -> object:
        if (isinstance(__other, Number)):
            return (Vector3(self.x >> __other, self.y >> __other, self.z >> __other))
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (Vector3(self.x >> __other.x, self.y >> __other.y, self.z >> __other.z))
        if (hasattr(__other, "x")):
            return (Vector3(self.x >> __other.x, self.y >> __other.x, self.z >> __other.z))
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (Vector3(self.x, self.y, self.z))
            if (len(__other == 1)):
                return (Vector3(self.x >> __other[0], self.y >> __other[0], self.z >> __other[0]))
            if (len(__other > 2)):
                return (Vector3(self.x >> __other[0], self.y >> __other[1], self.z >> __other[2]))

    def __neg__(self) -> object:
        return (Vector3(-self.x, -self.y, -self.z))
    
    def __pos__(self) -> object:
        return (Vector3(+self.x, +self.y, +self.z))
    
    def __abs__(self) -> object:
        return (Vector3(abs(self.x), abs(self.y), abs(self.z)))
    
    def __invert__(self) -> object:
        return (Vector3(~self.x, ~self.y, ~self.z))
    
    def __round__(self, __ndigit: int = None) -> object:
        return (Vector3(round(self.x, __ndigit), round(self.y, __ndigit), round(self.z, __ndigit)))
    
    def __hash__(self) -> int:
        return (hash(self))

    def __len__(self) -> int:
        return (3)
    
    def __getitem__(self, __key: int) -> int:
        if (__key > 2 or __key < -3):
            raise IndexError
        if (__key == 0 or __key == -3):
            return (self.x)
        if (__key == 1 or __key == -2):
            return (self.y)
        if (__key == 2 or __key == -1):
            return (self.z)

    def __setitem__(self, __key: int, __value: int):
        if (__key > 2 or __key < -3):
            raise IndexError
        if (__key == 0 or __key == -3):
            self.x = __value
        if (__key == 1 or __key == -2):
            self.y = __value
        if (__key == 2 or __key == -1):
            self.z = __value

    def __delitem__(self, __key: int) -> int:
        if (__key > 2 or __key < -3):
            raise IndexError
        if (__key == 0 or __key == -3):
            self.x = 0
        if (__key == 1 or __key == -2):
            self.y = 0
        if (__key == 2 or __key == -1):
            self.z = 0

    def __reversed__(self) -> object:
        return (Vector3(self.z, self.y, self.x))
    
    def __contains__(self, __item) -> bool:
        return (True if __item == self.x or __item == self.y or self.z == __item else False)
    
    def __eq__(self, __other: object) -> bool:
        if (isinstance(__other, Number)):
            return (self.x == __other and self.y == __other and self.z == __other)
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (self.x == __other.x and self.y == __other.y and self.z == __other.z)
        if (hasattr(__other, "x")):
            return (self.x == __other.x and self.y == __other.x and self.z == __other.x)
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (self.x == 0 and self.y == 0 and self.z == 0)
            if (len(__other == 1)):
                return (self.x == __other[0] and self.y == __other[0] and self.z == __other[0])
            if (len(__other > 2)):
                return (self.x == __other[0] and self.y == __other[1] and self.y == __other[2])
            
    def __ne__(self, __other: object) -> bool:
        if (isinstance(__other, Number)):
            return (self.x != __other and self.y != __other and self.z != __other)
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (self.x != __other.x and self.y != __other.y and self.z != __other.z)
        if (hasattr(__other, "x")):
            return (self.x != __other.x and self.y != __other.x and self.z != __other.x)
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (self.x != 0 and self.y != 0 and self.z != 0)
            if (len(__other == 1)):
                return (self.x != __other[0] and self.y != __other[0] and self.z != __other[0])
            if (len(__other > 2)):
                return (self.x != __other[0] and self.y != __other[1] and self.y != __other[2])
            
    def __lt__(self, __other: object) -> bool:
        if (isinstance(__other, Number)):
            return (self.x < __other and self.y < __other and self.z < __other)
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (self.x < __other.x and self.y < __other.y and self.z < __other.z)
        if (hasattr(__other, "x")):
            return (self.x < __other.x and self.y < __other.x and self.z < __other.x)
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (self.x < 0 and self.y < 0 and self.z < 0)
            if (len(__other == 1)):
                return (self.x < __other[0] and self.y < __other[0] and self.z < __other[0])
            if (len(__other > 2)):
                return (self.x < __other[0] and self.y < __other[1] and self.y < __other[2])
            
    def __le__(self, __other: object) -> bool:
        if (isinstance(__other, Number)):
            return (self.x <= __other and self.y <= __other and self.z <= __other)
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (self.x <= __other.x and self.y <= __other.y and self.z <= __other.z)
        if (hasattr(__other, "x")):
            return (self.x <= __other.x and self.y <= __other.x and self.z <= __other.x)
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (self.x <= 0 and self.y <= 0 and self.z <= 0)
            if (len(__other == 1)):
                return (self.x <= __other[0] and self.y <= __other[0] and self.z <= __other[0])
            if (len(__other > 2)):
                return (self.x <= __other[0] and self.y <= __other[1] and self.y <= __other[2])
            
    def __gt__(self, __other: object) -> bool:
        if (isinstance(__other, Number)):
            return (self.x > __other and self.y > __other and self.z > __other)
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (self.x > __other.x and self.y > __other.y and self.z > __other.z)
        if (hasattr(__other, "x")):
            return (self.x > __other.x and self.y > __other.x and self.z > __other.x)
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (self.x > 0 and self.y > 0 and self.z > 0)
            if (len(__other == 1)):
                return (self.x > __other[0] and self.y > __other[0] and self.z > __other[0])
            if (len(__other > 2)):
                return (self.x > __other[0] and self.y > __other[1] and self.y > __other[2])
            
    def __ge__(self, __other: object) -> bool:
        if (isinstance(__other, Number)):
            return (self.x >= __other and self.y >= __other and self.z >= __other)
        if (hasattr(__other, "x") and hasattr(__other, "y") and hasattr(__other, "z")):
            return (self.x >= __other.x and self.y >= __other.y and self.z >= __other.z)
        if (hasattr(__other, "x")):
            return (self.x >= __other.x and self.y >= __other.x and self.z >= __other.x)
        if (isinstance(__other, Iterable)):
            if (len(__other == 0)):
                return (self.x >= 0 and self.y >= 0 and self.z >= 0)
            if (len(__other == 1)):
                return (self.x >= __other[0] and self.y >= __other[0] and self.z >= __other[0])
            if (len(__other > 2)):
                return (self.x >= __other[0] and self.y >= __other[1] and self.y >= __other[2])
            
    def to_list(self) -> list:
        return [self.x, self.y, self.z]

def vector2_distance(__vec: Vector3, __second_vec: Vector3) -> float:
    return (
        sqrt(
            pow(__second_vec.x - __vec.x, 2) +
            pow(__second_vec.y - __vec.y, 2) +
            pow(__second_vec.z - __vec.z, 2)
        )
    )

def vector3_form_pos(pos_origin: Vector3, pos_end: Vector3) -> Vector3:
    return (Vector3(
        pos_end.x - pos_origin.x,
        pos_end.y - pos_origin.y,
        pos_end.z - pos_origin.z
    ))