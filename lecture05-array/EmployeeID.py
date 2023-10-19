n = int(input())
arr = list(map(int, input().split()))


def empty_id(n, arr):
    for i in range(1, n + 1):
        # find i
        is_found = False
        for j in range(n):
            if arr[j] == i:
                is_found = True
                break

        if is_found == False:
            return i

    return n+1


print(empty_id(n, arr))
