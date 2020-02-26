import redis
import time

conn = redis.Redis(host="127.0.0.1", port="6379", db=0)
# conn.rpush("sort-input", 23, 15, 110, 7)
# print(conn.sort("sort-input"))
# print(conn.sort("sort-input", alpha=True)) # 根据字母表顺序
# conn.hset("d-7", "field", 5)
# conn.hset("d-15", "field", 1)
# conn.hset("d-23", "field", 9)
# conn.hset("d-110", "field", 3)
# print(conn.sort("sort-input", by="d-*->field"))

# print(conn.keys("*"))
# print(conn.set("key", "value"))
# print(conn.get("key"))
# print(conn.expire("key", 2))  # 过期
# print(conn.get("key"))
# print(conn.ttl("key"))          # 检查过期时间
# time.sleep(2)
# print(conn.get("key"))
