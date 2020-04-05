'''
Author       : ajin
Date         : 2020-04-04 14:49:36
Description  : 
email        : ajin_w@163.com
那曾梦想屠龙的少年，终会变成油腻的中年大叔，端坐于显示器前，从指尖流淌的代码，终会改变整个世界
'''

class User:
    Object_var = 333
    def __init__(self, name):
        self.name = name
        self._age = None
    

    # 这里的age和类里面的age必须不同, 如果相同会导致无限获取递归
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, val):
        self._age = val

    # 查找不到属性的时候, 就会进入此方法
    def __getattr__(self, item):
        return "not found item"
    
    # def __getattribute__(self, item):
    #     return "无条件直接进入此方法, 比getatttr更优先, 是所有访问属性的入口"

if __name__ == "__main__":
    user = User("ajin")
    print(user.age)
    user.age = 2
    print(user.age)
    print(user.birth)
    print(User.__mro__)
    print(user.__dict__)
    print(User.__dict__)