def simple():
    print("started")
    x = yield
    print("recived:", x)

# my = simple()
# print(my)
# next(my)
# my.send(42)


def simple_gen(a):
    print("started a:", a)
    b = yield a
    print("recived b:", b)
    c = yield a + b
    print("recived c:", c)

my = simple_gen(12)
from inspect import getgeneratorstate
print(getgeneratorstate(my))
next(my)
print(getgeneratorstate(my))
my.send(28)
my.send(99)
print(getgeneratorstate(my))

