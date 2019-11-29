s = "Café" # 是四个Unicode字符
print(len(s))  # 转换为字节(bytes)对象
b = s.encode("utf-8")
print(b)
print(len(b))
print(b.decode()) # 转换为str对象

print("-"*10)
cafe = bytes("café", encoding = "utf8")
print(cafe)
print(cafe[0]) # 是range(256)以内的整数
# print(cafe[-1]) # 还是bytes类型
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[:1])
print(cafe_arr[-1:])

import array
num = array.array('h', [-2, -1, 0, 1, 2])  # 有符号整数
print(num)
print(bytes(num))