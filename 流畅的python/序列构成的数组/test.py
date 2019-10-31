symbols = "$*~:<SAD}^%"
codes = []
for i in symbols:
    codes.append(ord(i))
print(codes)
codes = [ ord(i) for i in symbols]
print(codes)
beyound_ascii = [ord(i) for i in symbols if ord(i) > 100]
print(beyound_ascii)
beyound_ascii = list(filter(lambda x: x>100, map(ord, symbols)))
print(beyound_ascii)

# 生成器表达式
print(tuple(ord(i) for i in symbols))
import array
print(array.array('I', (ord(i) for i in symbols)))

# 把元组用作记录
lax_coordinates = (33.9435, -118.408095)
city, year, pop, chg, area = ("tokyo", 2003, 32450, 0.66, 8014)
traveler_ids = [("USA", "31195855"), ("BRA", "CE342567"), ("ESP", "XDA205856")]
for passport in sorted(traveler_ids):
    print("%s/%s" % passport)

for country, _ in traveler_ids:
    print(country)