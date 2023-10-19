n = int(input())
arr = list(map(int, input().split()))


def count_pruning(default, job):
    if job - default > 0:
        return job - default

    return 0


def min_pruning(arr):
    min = arr[0]
    for i in range(1, n):
        if arr[i] < min:
            min = arr[i]

    return min


count = 0
default = min_pruning(arr)

for i in range(n):
    count += count_pruning(default, arr[i])

print(count)
