
a, b = map(int, input().split(" "))


def greatest_divisor(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return greatest_divisor(a % b, b)
    if b >= a:
        return greatest_divisor(a, b % a)


rs = greatest_divisor(a, b)
print(rs)
