'''
Author       : ajin
Date         : 2020-04-04 17:50:19
Description  : 
email        : ajin_w@163.com
那曾梦想屠龙的少年，终会变成油腻的中年大叔，端坐于显示器前，从指尖流淌的代码，终会改变整个世界
'''

class UserMetaClass(type):
    def __new__(cls, *args, **kwargs):
        print('create:  ' + str(args[0]))
        return super().__new__(cls, *args, **kwargs)
    

class BaseUser(metaclass=UserMetaClass):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "base user name:" + self.name


class User(BaseUser):
    pass


if __name__ == "__main__":
    user = User("test")
    print(user)