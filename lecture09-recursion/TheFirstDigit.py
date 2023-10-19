n = int(input())


def count_number(n):
    if n < 0:
        n = -n

    if n < 10:
        return n

    return count_number(n // 10)


rs = count_number(n)
print(rs)
