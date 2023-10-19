a = int(input())


def max_number(a):
    max = 0

    while a > 0:
        last = a % 10
        a //= 10

        if last > max:
            max = last

    return max


total = max_number(a)

print(total)
