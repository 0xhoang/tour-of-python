n = int(input())
arr = list(map(int, input().split()))


def compare_student(n, arr):
    count_girl = 0
    count_boy = 0

    for i in range(n):
        if arr[i] == 0:
            count_boy += 1

        if arr[i] == 1:
            count_girl += 1

    if count_girl == count_boy:
        return "YES"

    else:
        return "NO"


print(compare_student(n, arr))
