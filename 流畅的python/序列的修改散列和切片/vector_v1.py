from array import array
import reprlib
import math

class Vector2d:
    shortcut_names = "xyzt"
    typecode = 'd'
    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):  # 可迭代, 可拆包
        return iter(self._components)  # 这里必须返回的是可迭代的

    def __repr__(self):
        components = reprlib.repr(self._components) # 优先序列表示[1,2...]
        components = components[components.find("["):-1] # 去掉array的d和最后的]
        return "(vector {})".format(components)
    
    def __str__(self):  # 这里显示给用户看的
        return str(tuple(self))  

    def __bytes__(self):
        return (bytes([ord(self.typecode)] ) + bytes(self._components))

    def __eq__(self, value):
        return tuple(self) == tuple(value)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec = ""):
        compontents = (format(c, format_spec) for c in self)
        return "({},{})".format(*compontents)

    def __len__(self):
        return len(self._components)
    
    def __getitem__(self, index):
        return self._components[index]
    
    # @property
    # def x(self):
    #     return self.__x

    # @property
    # def y(self):
    #     return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    
    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if pos >=0 and pos <= len(self._components):
                return self._components[pos]
        msg = "{.__name__!r} object has no attr {!r}"
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = "readonly attr {attr_name!r}"
            elif name.islower():
                error = "can not set attr 'a' - 'a' in {cls_name!r}"
            else:
                error = ""
            if error:
                msg = error.format(cls_name = cls.__name__, attr_name = name)
                raise AttributeError(msg)
        super().__setattr__(name, value)



v1 = Vector2d([3, 1, 4, 2])
print(v1)
v2 = Vector2d(range(10))
print(v2[2:5])
print(v2[2:8:2])
print(v2)
print(v2.x)
print(v2.t)

