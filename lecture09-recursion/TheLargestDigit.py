n = int(input())


def max_number(n):
    if n < 0:
        n = -n

    if n < 10:
        return n

    digit = n % 10
    max = digit

    num = max_number(n // 10)
    if max < num:
        max = num

    return max


rs = max_number(n)
print(rs)
