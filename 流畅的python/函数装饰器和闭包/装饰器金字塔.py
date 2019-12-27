import time

default_fmt = "[{elapsed:0.8f}s] {name}({args}) -> {result}"

def clock(fmt = default_fmt):
    def decorate(func):
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
            print(fmt.format(**locals()))
            return result
        return clocked
    return decorate


if __name__ == '__main__':
    # @clock()
    # def snooze(seconds):
    #     time.sleep(seconds)
    
    # for i in range(3):
    #     snooze(0.123)

    @clock("{name}: {elapsed}")
    def snooze(seconds):
        time.sleep(seconds)
     
    for i in range(3):
        snooze(0.123)
    