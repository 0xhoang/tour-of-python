n, x = input().split()
list = list(map(int, input().split()))


def findX(list, n, x):
    for i in range(n):
        if list[i] == x:
            return i + 1

    return -1


print(findX(list, int(n), int(x)))
