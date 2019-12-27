### 对象可拆包必须实现iter方法
### self 是init里面定义的self值
### repr是给开发者看的, 使用repr(object)
### eq是类实例的等于

## classmethod和staticmethod
classmethod定义操作类, 而不是操作示例的方法, 改变了调用方法的方式, 传入的第一个参数是类本身, 而不是实例, staticmethod就是普通函数

## 获得属性使用@property, 类似与obj.x

## 实现hash可使对象变成可散列的

## 名称改写来实现私有变量
在使用两个下划线命名的属性, 会把属性名存入dict属性中, 并且是`_obj__mode`这样存储, 但是如果是单个下划线不会做处理

## 使用`__slots__`节省空间
1. dict是占用空间的, 但是将属性放入slots后会节省大量空间
2. 定义slots属性后, 示例不能再由其他名称属性
3. 如果需要弱引用, 那么就要把`__weakref__`填入slots


``` python
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
```