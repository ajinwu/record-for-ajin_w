def genera():
    print("start")
    yield "A"
    print("continue")
    yield "B"
    print("end")

res1 = [x * 3 for x in genera()]
print(res1)
for i in res1:
    print(i)

res2 = (x * 3 for x in genera())
print(" res2:",res2)
for i in res2:
    print(i)