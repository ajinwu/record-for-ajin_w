import random
class Bingocage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
    def pick(self):
        try:
            return self._items.pop()
        except:
            raise "pick is None"
    def __call__(self):
        return self.pick()

bingo = Bingocage(range(3))
print(bingo.pick())
print(callable(bingo))