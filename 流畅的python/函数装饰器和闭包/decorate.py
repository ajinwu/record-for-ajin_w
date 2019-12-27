import time

# def clock(func):
#     def clocked(*args):
#         t0 = time.perf_counter()
#         result = func(*args)
#         elapsed = time.perf_counter() - t0
#         name = func.__name__
#         arg_str = ", ".join(repr(arg) for arg in args)
#         print("[%0.8fs] %s(%s) ->%r" %(elapsed, name, arg_str, result))
#         return result
#     return clocked

def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(", ".join(str(arg) for arg in args))
        if kwargs:
            pairs = ["%s=%r" %(k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(", ".join(pairs))
        arg_str = ", ".join(arg_list)
        print("[%0.8fs] %s(%s) ->%r" %(elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def factor(n):
    return 1 if n < 2 else n * factor(n - 1)

@clock
def soonze(seconds):
    time.sleep(seconds)


if __name__ == '__main__':
    print("calling snooze(.123)")
    soonze(0.123)
    print("calling fatoer")
    print("6!=", factor(6))
    