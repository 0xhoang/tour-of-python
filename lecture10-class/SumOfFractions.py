a, b = map(int, input().split())
c, d = map(int, input().split())


class Fractions:
    def __init__(self, a1, b1, a2, b2):
        self.a1 = a1
        self.b1 = b1

        self.a2 = a2
        self.b2 = b2

    def shorten(self, a, b):
        point = a
        if a > b:
            point = b

        for i in range(point - 1, 0, -1):
            if a % i == 0 and b % i == 0:
                a = a // i
                b = b // i

        return a, b

    def add(self):
        a = self.a1 * self.b2 + self.a2 * self.b1
        b = self.b1 * self.b2

        return self.shorten(a, b)


my_class = Fractions(a, b, c, d)
a, b = my_class.add()

print(a, b)
