n = int(input())


def biggest_old_divisor(n):
    if n % 2 != 0:
        return n

    return biggest_old_divisor(n / 2)


rs = biggest_old_divisor(n)
print("{:.0f}".format(rs))
