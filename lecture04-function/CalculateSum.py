number = int(input())


def sqrt(n):
    return n * n


total = 0
for i in range(1, number + 1):
    total += sqrt(i)

print(total)