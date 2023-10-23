import math

a, b = map(int, input().split())
n = int(input())


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, z, t):
        a = self.x - z
        b = self.y - t

        return math.sqrt(a ** 2 + b ** 2)


my_class = MyClass(a, b)

max = 0
max_x = 0
max_y = 0

for i in range(n):
    x, y = map(int, input().split())
    value = my_class.distance(x, y)
    if value > max:
        max = value
        max_x = x
        max_y = y

print(max_x, max_y)
