from array import array

import math

class Vector2d:
    typecode = 'd'
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):  # 可迭代, 可拆包
        return (i for i in (self.x, self.y))  # 这里必须返回的是可迭代的

    def __repr__(self):
        class_name = type(self).__name__
        return "{} ({!r}, {!r})".format(class_name, *self)  # 获取分量的提供给format
    
    def __str__(self):  # 这里显示给用户看的
        print(*self)
        return str(tuple(self))  

    def __bytes__(self):
        return (bytes([ord(self.typecode, self)] ) + bytes(array(self.typecode, self)))

    def __eq__(self, value):
        return tuple(self) == tuple(value)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec = ""):
        compontents = (format(c, format_spec) for c in self)
        return "({},{})".format(*compontents)
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    


v1 = Vector2d(1, 2)
print(list(v1))
print(v1)
print(repr(v1))
v2 = Vector2d(3, 2)
print(v1 == v2)
print(format(v1))
print(set([v1, v2]))