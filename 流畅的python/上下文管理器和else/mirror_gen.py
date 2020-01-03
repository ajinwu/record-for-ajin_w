import contextlib

@contextlib.contextmanager
def looking():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])
    
    sys.stdout.write = reverse_write
    msg = ""
    try:
        yield "ABCDE"
    except ZeroDivisionError:
        mgs = " by zero"
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


with looking() as what:
    print("yhn")
    print(what)

