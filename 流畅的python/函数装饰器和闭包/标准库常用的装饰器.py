# 使用缓存实现加速计算
from functools import lru_cache
from decorate import clock

# @lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

if __name__ == '__main__':
    print(fibonacci(40))
    