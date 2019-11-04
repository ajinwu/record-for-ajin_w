from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
with open("./floats.txt", "wb") as f:
    floats.tofile(f)

float2 = array('d')
with open("./floats.txt", "rb") as f:
    float2.fromfile(f, 10**7)
print(float2[-1])
print(float2 == floats)