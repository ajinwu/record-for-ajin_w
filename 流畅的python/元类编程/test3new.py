'''
Author       : ajin
Date         : 2020-04-04 16:54:01
Description  : 
email        : ajin_w@163.com
那曾梦想屠龙的少年，终会变成油腻的中年大叔，端坐于显示器前，从指尖流淌的代码，终会改变整个世界
'''
class User(object):
    def __new__(cls, *args, **kwarg):
        print("in new")
        return super().__new__(cls)
    
    def __init__(self, name):
        print("in init")
        self.name = name

if __name__ == "__main__":
    user = User("ajin")