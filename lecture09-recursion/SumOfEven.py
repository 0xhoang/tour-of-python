import  sys
sys.setrecursionlimit(1000000)

n = int(input())
list = list(map(int, input().split(" ")))


def sum_even_number(n, list):
    if n < 0:
        return 0

    if list[n] % 2 == 0:
        return list[n] + sum_even_number(n - 1, list[:n])

    return sum_even_number(n - 1, list[:n])


rs = sum_even_number(n - 1, list)
print(rs)
