def test(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

# test(1, 2, 3, 4, e=5, f=6, g=7)


def test2(a:int, b: int=10, **args):
    print(a)
    print(b)
    # print(arg)
    print(args)

test2(1, 2,  e=5, f=6, g=7)


print(test2.__defaults__)
print(test2.__code__.co_varnames)
print(test2.__code__.co_argcount)
print(test.__annotations__)

from inspect import signature
sig = signature(test2)
print(str(sig))
for name, param in sig.parameters.items():
    print(param.kind, ":", name, "=", param.default)

from functools import partial
from operator import mul
partial = partial(mul, 7)
print(partial(3))
print(list(map(partial, range(5))))