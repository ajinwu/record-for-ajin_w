'''
Author       : ajin
Date         : 2020-04-04 16:05:07
Description  : 
email        : ajin_w@163.com
那曾梦想屠龙的少年，终会变成油腻的中年大叔，端坐于显示器前，从指尖流淌的代码，终会改变整个世界
'''
import numbers
class IntField:
    # 只要实现(get, set, delete其中任何一种方法, 他都是属性描述符), 实现了get,set两种, 称之为数据描述符
    # 属性描述夫, 数据描述符
    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, val):
        if not isinstance(val, numbers.Integral):
            raise ValueError("must need int value")
        self.val = val

    def __delete__(self, instance):
        pass

class NoneDataIntField:
    # 属性描述符, 非数据描述符
    def __get__(self, instance, owner):
        return self.val

class User:
    age = IntField()

if __name__ == "__main__":
    user = User()
    user.age = 30
    print(user.age)
    print(getattr(user, "age"))



# 如果user是某个类的实例(User), 那么user.age等价于getattr(user, "age")
# 首先调用__getattribute__, 如果类也定义了__getattr__方法, 那么在__getattribute__抛出异常之前会进入__getattr__
# 而对于属性描述符(__get__)的调用, 会发生在__getattribute__的内部
# user = User(), 那么user.age调用顺序如下
# 1. 如果age出现在User类或者其父类的__dict__中, 且age是数据描述符, 则会调用其__get__方法, 否则
# 2. 如果age出现在user对象的__dict__中, 那么就会直接返回user.__dict__["age"], 否则
# 3. 如果age出现在User类或者父类的__dict__中
# 3.1 如果是age是非数据描述符, 那么调用__get__方法, 否则
# 3.2 返回__dict__["age"]
# 4. 如果有__getattr__函数, 就会转入调用
# 5. 跑出attributeerror异常