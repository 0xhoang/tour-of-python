def insert_sort(a, n):
    j = n
    while j > 0 and a[j - 1] > a[j]:
        a[j], a[j - 1] = a[j - 1], a[j]
        j -= 1

    return a


def sort(list, n):
    for i in range(len(list)):
        insert_sort(list, i)

    if n % 2 == 0:
        median = n // 2
        return (list[median - 1] + list[median]) / 2

    median = n // 2 + 1
    return list[median - 1]


n = int(input())
list_item = list(map(int, input().split()))

print(sort(list_item, n))
