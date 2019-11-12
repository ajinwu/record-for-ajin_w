from collections import UserDict
class user_dict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def __contains__(self, key):
        return str(key) in self.data # data是一个dict实例
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item

d = user_dict([("2", "two"), ("4", "four")])
print(d["2"])
print(d.get("2"))
print(d.get(4))
print(d.get(1,"None"))
print(2 in d)
print(1 in d)
print(d.data.keys())
print(d[1])