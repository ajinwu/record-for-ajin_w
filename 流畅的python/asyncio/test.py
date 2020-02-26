import asyncio
import itertools
import sys

@asyncio.coroutine
def Spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle("|/-\\"):
        status = char + " " +msg
        write(status)
        flush()
        write("\x08" * len(status))
        try:
            yield from asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
        
    write(" " * len(status) + "\x08" * len(status))

@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(3)
    return 42

@asyncio.coroutine
def supervisor():
    spinner = asyncio.ensure_future(Spin("thinking!"))
    print("spinner object:", spinner)
    result = yield from slow_function()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close
    print("answer:", result)

if __name__ == "__main__":
    main() 