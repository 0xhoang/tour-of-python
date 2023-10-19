a, b = map(int, input().split())


def fraction(a, b):
    gcd = 1
    min = a
    if a > b:
        min = b

    for i in range(1, min + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    c = a // gcd
    d = b // gcd

    return c, d


c, d = fraction(a, b)

print("{} {}".format(c, d))
