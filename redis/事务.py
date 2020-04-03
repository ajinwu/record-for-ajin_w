'''
Author       : ajin
Date         : 2019-12-29 16:51:34
Description  : 
email        : ajin_w@163.com
那曾梦想屠龙的少年，终会变成油腻的中年大叔，端坐于显示器前，从指尖流淌的代码，终会改变整个世界
'''
import redis
import threading
import time

conn = redis.Redis(host="127.0.0.1", port="6379", db=0)

def notrans():
    # multi  exec, 从multi开始,所有的命令会放进一个队列, 知道exec命令出现结束, pipline是一种实现
    pipeline = conn.pipeline()
    print(pipeline.incr("notrans:"))
    time.sleep(0.1)
    pipeline.incr("notrans:", -1)
    print(pipeline.execute()[0])

if 1:
    for i in range(3):
        threading.Thread(target=notrans).start()
    time.sleep(0.5)