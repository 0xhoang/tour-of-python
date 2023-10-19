n = int(input())
hour = list(map(int, input().split()))


def plain_learning(n, arr):
    prev = arr[0]

    check_computer = 0
    if prev == 0:
        check_computer += 1

    for i in range(1, n):
        if arr[i] != prev:
            if arr[i] == 0:
                check_computer = 1
            else:
                check_computer = 0

            prev = arr[i]
            continue

        if arr[i] == prev and arr[i] == 0:
            check_computer += 1
            prev = arr[i]

            if check_computer > 3:
                return "NO"

    if arr[n - 1] != 1:
        return "NO"

    return "YES"


print(plain_learning(n, hour))
