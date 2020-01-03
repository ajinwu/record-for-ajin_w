from random import randrange

from tombola import Tombola

@Tombola.register
class TomoList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError("pop error")
    
    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


print(issubclass(TomoList, Tombola))
t = TomoList(range(100)) 
print(isinstance(t, Tombola))
print(issubclass(t, Tombola))