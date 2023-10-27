def insert_sort(a, n, x):
    j = n
    while j > 0:
        if a[j - 1] <= x:
            break

        a[j] = a[j - 1]
        j -= 1

    a[j] = x


def sort(list):
    # insert sort
    for i in range(len(list)):
        x = list[i]
        insert_sort(list, i, x)

    return list


n = int(input())
list_item = list(map(int, input().split()))

list = sort(list_item)
for i in range(n):
    print(list[i], end=' ')
