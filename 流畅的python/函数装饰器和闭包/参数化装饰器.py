registry = set()

def register(active = True):
    def decorate(func):
        print("running register(active=%s) ->decorate(%s)" %(active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate

@register(active=False)
def f1():
    print("running f1")

@register()
def f2():
    print("running f2")

def f3():
    print("running f3")

print(register()(f3))
print(register()(f2))
print(registry)
