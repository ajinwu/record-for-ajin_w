t = (20, 8)
print(divmod(*t))
a, b, *rest = range(5)
print(a, b, rest)
a, *b, rest= range(5)
print(a,b,rest)
print("*"*10)
print(tuple(b))

from collections import namedtuple
City = namedtuple("City", "name country population coordinates")
tokyo = City("City", "JP", 36.933, (35.689722, 139.69177))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)

print(City._fields)
LatLong = namedtuple("LatLong", "lat long")
delhi_data = ("Delhi NCR", "IN", 21.935, LatLong(28.61389, 77.20889))
delhi = City._make(delhi_data) # 通过接受一个可迭代对象来生成这个类的一个实例,跟City(*delhi_data)同理
print(delhi)
for key, value in delhi._asdict().items():
    print(key+":",value)

a = (1,2)
b = (3,4)
print(a.__add__(b))
print(id(a),id(a.__mul__(3)))