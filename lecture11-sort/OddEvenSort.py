def insert_sort(a, n):
    j = n
    while j > 0 and a[j - 1] > a[j]:
        a[j], a[j - 1] = a[j - 1], a[j]
        j -= 1

    return a


def insert_sort_desc(a, n):
    j = n
    while j > 0 and a[j - 1] < a[j]:
        a[j], a[j - 1] = a[j - 1], a[j]
        j -= 1

    return a


def sort(list):
    # insert sort

    even_list = []
    odd_list = []
    for i in range(len(list)):
        x = list[i]
        if x % 2 == 0:
            even_list.append(x)
        else:
            odd_list.append(x)

    for i in range(len(even_list)):
        insert_sort(even_list, i)

    for i in range(len(odd_list)):
        insert_sort_desc(odd_list, i)

    jj = ii = 0

    for i in range(len(list)):
        x = list[i]
        if x % 2 == 0:
            print(even_list[ii], end=' ')
            ii += 1
        else:
            print(odd_list[jj], end=' ')
            jj += 1


n = int(input())
list_item = list(map(int, input().split()))
sort(list_item)
