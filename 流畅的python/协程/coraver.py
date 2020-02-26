from collections import namedtuple

Result = namedtuple("Result", "count average")

def averager():
    total = 0.0
    count = 0
    avergae = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        avergae = total / count
    return Result(count, avergae)

av = averager()
next(av)
av.send(10)
av.send(30)
try:
    av.send(None)
except StopIteration as exc:
    result = exc.value
print(result) 