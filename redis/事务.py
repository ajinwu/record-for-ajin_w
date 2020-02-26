import redis
import threading
import time

conn = redis.Redis(host="127.0.0.1", port="6379", db=0)

def notrans():
    pipeline = conn.pipeline()
    print(pipeline.incr("notrans:"))
    time.sleep(0.1)
    pipeline.incr("notrans:", -1)
    print(pipeline.execute()[0])

if 1:
    for i in range(3):
        threading.Thread(target=notrans).start()
    time.sleep(0.5)