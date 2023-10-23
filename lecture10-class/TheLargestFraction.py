class Fractions:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class CompareFractions:
    def __init__(self, list_fractions):
        self.list_fractions = list_fractions

    def shorten(self, a, b):
        point = a
        if a > b:
            point = b

        if a == 0:
            point = b

        for i in range(point, 0, -1):
            if a % i == 0 and b % i == 0:
                a = a // i
                b = b // i

        return a, b

    def find_max(self):
        min_a = self.list_fractions[0].a
        min_b = self.list_fractions[0].b

        for i in range(len(self.list_fractions) - 1):
            item1 = min_a * self.list_fractions[i + 1].b
            item2 = self.list_fractions[i + 1].a * min_b

            item_total = min_b * self.list_fractions[i + 1].b

            min_b = item_total
            if item1 > item2:
                min_a = item1
            else:
                min_a = item2

            min_a, min_b = self.shorten(min_a, min_b)

        return self.shorten(min_a, min_b)


list = []
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    list.append(Fractions(a, b))

my_class = CompareFractions(list)
a, b = my_class.find_max()

print(a, b)
