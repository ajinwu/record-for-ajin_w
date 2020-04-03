'''
Author       : ajin
Date         : 2020-02-27 13:56:19
Description  : 
email        : ajin_w@163.com
ajin是最好的人啦
'''

class test:
    t = 0
    def __init__(self):
        pass

    @classmethod
    def add(cls):
        cls.t += 1

t1 = test()
t1.add()
print(t1.t)
t2 = test()
print(t2.t)