a = int(input())


def count_number(a):
    count = 0

    while a > 0:
        count += 1
        a //= 10

    return count


total = count_number(a)

print(total)
