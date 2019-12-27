t1 = (1, 2, 3)
t2 = tuple(t1)
print(t1 is t2)  # True
t3 = t1[:]
print(t1 is t3) # True

s1 = (1, 2, 3)
s2 = (1, 2, 3)
print(s1 is s2) # True
w1 = "ABC"
w2 = "ABC"
print(w1 is w2) # True
