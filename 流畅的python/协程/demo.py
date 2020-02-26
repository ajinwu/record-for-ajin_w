class Demo(Exception):
    pass

def demo():
    print("started")
    while True:
        try:
            x = yield
        except Demo:
            print("demo exception")
        else:
            print("recived: {!r}".format(x))
    raise RuntimeError("error")

exc = demo()
next(exc)
exc.send(11)
exc.send(12)
from inspect import getgeneratorstate
print(getgeneratorstate(exc))