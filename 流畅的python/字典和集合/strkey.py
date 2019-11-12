class strkey(dict):
    # 再找不到键的时候会在这里进行字符装换
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default = None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d = strkey([("2", "two"), ("4", "four")])
print(d["2"])
print(d.get("2"))
print(d.get(4))
print(d.get(1,"None"))
print(2 in d)
print(1 in d)
print(d[1])


