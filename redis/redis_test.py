import redis
conn = redis.Redis(host = '127.0.0.1', port = 6379, db = 0)
print(conn.get('key'))

# 阻塞操作, 在等待的时间内如果出现了才会继续操作, 没有数据会直接返回None
print(conn.brpoplpush('list', 'list2', 1))
print(conn.lrange('list', 0, -1))
print(conn.lrange('list2', 0, -1))

print(conn.sadd("set-key", "a", "b", "c")) # set添加
print(conn.smembers("set-key"))  # 返回集合所有成员
print(conn.scard("set-key")) # 返回集合 key 的基数(集合中元素的数量)。
print(conn.sismember("set-key", "a")) # 是否存在与集合
print(conn.srandmember("set-key", 1)) # 整数不重复， 负数会重复
print(conn.srem("set-key", "a"))      # 删除
print(conn.smove("set-key", "set-key2", "1")) # 移动
print(conn.smove("set-key", "set-key2", "c"))
print(conn.smembers("set-key"))
print(conn.smembers("set-key"))
print(conn.smembers("set-key2"))
print(conn.sdiff("set-key", "set-key2"))  # 差
print(conn.sinter("set-key", "set-key2")) # 交
print(conn.sunion("set-key", "set-key2")) # 并
print(conn.sdiffstore("set-key2", "set-key")) # 结果放入新集合
print(conn.smembers("set-key"))
print(conn.smembers("set-key2"))

print(conn.hset("hash-key","k", "v"))
print(conn.hget("hash-key", "k"))
print(conn.hgetall("hash-key"))
print(conn.hmset("hash-key", {"k1":"v1", "k2":"v2"}))
print(conn.hmget("hash-key", {"k", "k1"}))
print(conn.hlen("hash-key"))
print(conn.hdel("hash-key", "k"))
print(conn.hgetall("hash-key"))
print(conn.hexists("hash-key", "k0"))
print(conn.hkeys("hash-key"))
print(conn.hvals("hash-key"))
print(conn.hincrby("counter", "test", 200))  # 自增
print(conn.hincrby("counter", "test", -50))
print(conn.hget("counter", "test"))
print(conn.hdel("hash-key"))



print(conn.zadd("zset-key", {"a": 3, "b": 2, "c": 1}))    # 添加
print(conn.zcard("zset-key"))           # 数量
print(conn.zincrby("zset-key", 3, "c")) # 自增
print(conn.zscore("zset-key", "b"))     # 分值
print(conn.zrank("zset-key", "b"))      # 排名
print(conn.zcount("zset-key", 0, 3))    # 分值范围的总和
print(conn.zrem("zset-key", "b"))
print(conn.zrange("zset-key", 0, -1, withscores=True))        # 从小到大排序
print(conn.zrevrange("zset-key", 0, -1, withscores=True))     # 返回区间的元素排名, 成员按照分值大到小排列
print(conn.zrevrank("zset-key", 1)) # 不理解
print(conn.zrangebyscore("zset-key", 0, 3))
print(conn.zadd("zset-key", {"d":9, "e":8, "b":10}))
print(conn.zrange("zset-key", 0, -1, withscores=True))
print(conn.zremrangebyrank("zset-key", 1, 3))  # 按照分数排名从高到低删除
print(conn.zrange("zset-key", 0, -1, withscores=True))
conn.zadd("zset-1", {"a": 3})
conn.zadd("zset-2", {"b": 5})
print(conn.zunionstore("zset-0", ["zset-1", "zset-2"]))
print(conn.zrange("zset-0", 0, -1, withscores=True))
