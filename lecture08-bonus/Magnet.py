n = int(input())
item = []
for i in range(n):
    item.append(int(input()))


def magnet(n, list):
    first = list[0]
    count = 0
    for i in range(1, n):
        if list[i] != first:
            count += 1

        first = list[i]

    count += 1

    return count


print(magnet(n, item))
