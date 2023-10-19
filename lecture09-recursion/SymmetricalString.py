import sys

sys.setrecursionlimit(1000000)

n = int(input())
str = input()


def check_symmetrica(i, n, str):
    if i == n:
        return True

    if str[i] != str[n - 1 - i]:
        return False

    return check_symmetrica(i + 1, n, str)


rs = check_symmetrica(0, n, str)
if rs:
    print("YES")
else:
    print("NO")
