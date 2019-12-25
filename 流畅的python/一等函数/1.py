friuts = ["strawberry", "fig", "apple", "cheryy", "banana"]

# print(sorted(friuts, key = len))
print(friuts)
from typing import List
def reversed(word: List) ->List:
    return word[::-1]
print(sorted(friuts, key = reversed))


def fact(n: int) -> List:
    return 1 if n < 2 else n * fact(n - 1)
    # return n if n % 2 == 0 else 0

print(list(map(fact,range(6))))

print(list(map(fact, filter(lambda x:x % 2, range(6)))))

from functools import reduce
from operator import add

def add_(a: int, b: int) ->int:
    return a+b
print(reduce(add_, range(100)))

print({key:value for i in list(map(lambda x, y: {x : y}, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])) for key,value in i.items()})
print(dict(zip([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))

print(list(filter(lambda x:x%2, range(10))))
print(reduce(lambda x,y:x + y, range(100)))