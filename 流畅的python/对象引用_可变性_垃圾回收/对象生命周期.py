import weakref
# s1 = {1, 2, 3}
# s2 = s1
# def bye():
#     print("over")
# ender = weakref.finalize(s1, bye)  # 要有回调函数
# print(ender.alive)
# del s1
# print(ender.alive)
# s2 = "dsf"
# print(ender.alive)

s = {0, 1}
ref = weakref.ref(s)
print(ref)
print(ref())
s = {2,3}
print(ref())