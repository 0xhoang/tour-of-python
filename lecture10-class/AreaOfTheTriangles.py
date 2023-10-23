import math

n = int(input())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangles:
    def __init__(self, point1, point2, point3):
        self.a = point1
        self.b = point2
        self.c = point3

    def length2point(self, point1, point2):
        return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5

    def perimeter(self, a, b, c):
        return a + b + c

    def area(self):
        len1 = self.length2point(self.a, self.b)
        len2 = self.length2point(self.b, self.c)
        len3 = self.length2point(self.c, self.a)

        p = self.perimeter(len1, len2, len3) / 2
        s = (p * (p - len1) * (p - len2) * (p - len3)) ** 0.5

        return s


total = 0
for i in range(n):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    a = Point(x1, y1)
    b = Point(x2, y2)
    c = Point(x3, y3)

    d = Triangles(a, b, c)
    total += d.area()

print("{:.2f}".format(total))
