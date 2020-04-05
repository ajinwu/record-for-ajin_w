'''
Author       : ajin
Date         : 2020-04-04 17:11:01
Description  : 
email        : ajin_w@163.com
那曾梦想屠龙的少年，终会变成油腻的中年大叔，端坐于显示器前，从指尖流淌的代码，终会改变整个世界
'''
def create_metaclass(name):
    if name == "user":
        class User:
            def __str__(self):
                return "User"
        return User
    else:
        class Other:
            def __str__(self):
                return "other"
        return Other


def sayhello(self):
    return self.name   

class BaseClass:
    def answer(self):
        return "i am answer class" 

User = type("User", (BaseClass, ), {"name":"user", "sayhello":sayhello})   # type(object_or_name, bases, dict)   类名, 继承, 属性
    
if __name__ == "__main__":
    # myclass = create_metaclass("user")
    # print(myclass(), type(myclass()))
    my_obj = User()
    print(my_obj, my_obj.name, my_obj.sayhello(), my_obj.answer())