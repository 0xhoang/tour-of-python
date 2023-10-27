def isPrime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def insert_sort(a, n):
    j = n
    while j > 0 and a[j - 1] > a[j]:
        a[j], a[j - 1] = a[j - 1], a[j]
        j -= 1

    return a


def sort(list):
    # insert sort

    list_b = []
    for i in range(len(list)):
        x = list[i]
        if isPrime(x) == False:
            list_b.append(x)

    for i in range(len(list_b)):
        insert_sort(list_b, i)

    j = 0
    for i in range(len(list)):
        x = list[i]

        if isPrime(x) == True:
            print(list[i], end=' ')
        else:
            print(list_b[j], end=' ')
            j = j + 1


n = int(input())
list_item = list(map(int, input().split()))
sort(list_item)
