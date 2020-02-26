import time
import threading
import redis

conn = redis.Redis(host="127.0.0.1", port="6379", db=0)

def publisher(n: int):
    time.sleep(1)
    for i in range(n):
        conn.publish("channel", i+2)
        time.sleep(1)



def run_pubsub():
    t = threading.Thread(target=publisher, args=(3,))
    t.start()
    pubsub = conn.pubsub()
    pubsub.subscribe(["channel"])
    count = 0
    for item in pubsub.listen():
        print(item)
        count += 1
        if count == 4:
            pubsub.unsubscribe()
        if count == 5:
            break
run_pubsub()