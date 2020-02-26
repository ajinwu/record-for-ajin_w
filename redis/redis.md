[redis命令参考](http://redisdoc.com/sorted_set/zincrby.html)
[redis-python命令参考](https://redis-py.readthedocs.io/en/latest/)
# redis提供的5中数据结构

结构类型|结构存储的值|结构的读写能力|
--|--|--|
string | 可以是字符串, 整数, 或者浮点数 | 对整个字符串或者字符串中的一部分进行执行操作, 对整数和浮点数执行自增或者自减操作
list | 一个链表, 链表上的每个结点都包含一个字符串 | 从链表的两端推入或者弹出元素, 根据偏移量进行改变, 读取单个或者多个元素; 根据值查找或者移除元素
set | 无需集合 | 添加, 获取, 移除单个元素, 检查是否存在, 计算交并补, 随机读
hash | 包含键值对的无需散列表 | 添加, 获取, 移除单个键值对, 获取所有键值对
zset | 字符串和浮点数的有序映射 | 添加, 获取, 删除单个元素, 根据范围来获取元素

## string

命令 | 动作
--|--
get | 获取特定key的值
set | 设置特定key的值
del | 删除特定key的值


## list

命令 | 动作
--|--|
rpush/lpush | 将定值插入key某端
lrange | 获取范围内的key
lindex | 获取给定位置的value
lpop/rpop | 从某端弹出一个value
lindex | 返回偏移量的元素
ltrim | 只保留start到end的元素


## set

命令 | 动作
--|--|
sadd | 添加一个元素进入key, 1成功, 0存在
smember | 显示所有的元素
sismember | 是否存在与集合
srem | 删除

## hash散列表(字典)

命令 | 动作
--|--|
hset | 设置键值对
hget | 获取键的值
hgetall | 获取所有键值对
hdel | 删除键


## zset(有序集合)

命令 | 动作
--|--|
zadd | 讲一个带有分支的成员添加到有序集合里面
zrange | 根据元素所在位置获取多个元素
zrangebyscores | 根据分值范围获取元素
zrem | 如果存在则删除成员




``` python
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

```