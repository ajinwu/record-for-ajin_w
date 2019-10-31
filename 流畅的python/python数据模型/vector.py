from math import hypot
class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    # %r是一种格式化字符方法, 处理比较生硬, 会加上字符的引号
    def __repr__(self):
        return "Vector(%s, %s)" %(self.x , self.y)
    # 返回欧几里得解
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(self.x or self.y)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    

v1 = Vector(2, 4)
print(v1)
print(Vector(1,2) + Vector(3,4))
print(abs(Vector(-3, 4)))
print(v1 * 3)
print(eval(repr(v1)))