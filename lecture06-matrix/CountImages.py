m, n = map(int, input().split())


def count_image(m, n):
    total = 0

    for i in range(m):
        input_row = list(map(int, input().split()))
        for j in range(n):
            if input_row[j] > 100:
                total += 1

    return total


print(count_image(m, n))
