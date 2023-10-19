import sys

sys.setrecursionlimit(1000000)

n = int(input())
list = list(map(int, input().split(" ")))


def is_prime(n):
    if n < 1:
        return False

    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def first_prime(i, n, list):
    if i == n:
        return -1

    num = list[i]

    if is_prime(num):
        return i

    return first_prime(i + 1, n, list)


rs = first_prime(0, n, list)
print(rs)
