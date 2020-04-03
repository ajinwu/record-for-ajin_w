'''
Author       : ajin
Date         : 2020-02-27 13:40:13
Description  : 
email        : ajin_w@163.com
ajin是最好的人啦
'''


# 使用函数装饰器实现单例模式
def single(cls):
    _instance = {}
    def wrapper():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return wrapper

@single
class Test1:
    def __init__(self):
        pass

# print(id(Test1()) == id(Test1()))


# 类装饰器
class single2:
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}
    
    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls
        return self._instance[self._cls]

@single2
class Test2:
    def __init__(self):
        pass

# print(id(Test2()) == id(Test2()))


class Test3:
    _instance = None

    def __new__(cls, *args, **kwarg):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwarg)
        return cls._instance

    def __init__(self):
        pass

# print(id(Test3()) == id(Test3()))


class meta(type):
    _instance = {}

    def __call__(cls, *args, **kwarg):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwarg)
        return cls._instance


class Test4(metaclass = meta):
    def __init__(self):
        pass



print(id(Test4()) == id(Test4()))
