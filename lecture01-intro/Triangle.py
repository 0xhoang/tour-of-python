a, b, c = map(float, input().split())

perimeter = a + b + c
p = perimeter / 2
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5


print("{0:.2f} {1:.2f}".format(perimeter, area))
