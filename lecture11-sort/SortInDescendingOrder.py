def mergeDesc(L, n1, R, n2, a):
    i = j = k = 0

    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1

        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1


def mergeSortDesc(a, n):
    if n > 1:
        n1 = n // 2
        n2 = n - n1

        L = a[:n1]
        R = a[n1:]

        mergeSortDesc(L, n1)
        mergeSortDesc(R, n2)

        mergeDesc(L, n1, R, n2, a)

    return a


n = int(input())
list_item = list(map(int, input().split()))

list = mergeSortDesc(list_item, n)
for i in range(n):
    print(list[i], end=' ')
