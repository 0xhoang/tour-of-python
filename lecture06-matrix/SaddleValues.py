m, n = map(int, input().split())


def count_saddle(m, n):
    matrix = []

    for i in range(m):
        input_row = list(map(int, input().split()))
        row = []
        for j in range(n):
            row.append(input_row[j])

        matrix.append(row)

    count_saddle = 0
    for i in range(m):
        for j in range(n):
            if check_saddle(matrix, m, n, i, j):
                count_saddle += 1

    return count_saddle


def check_saddle(matrix, m, n, row, col):
    is_saddle = True

    max_num_of_row = matrix[row][col]

    # check max row
    for j in range(n):
        if matrix[row][j] > max_num_of_row:
            is_saddle = False
            break

    if is_saddle == False:
        return False

    # check max col
    for j in range(m):
        if matrix[j][col] < max_num_of_row:
            is_saddle = False
            break

    if is_saddle == False:
        return False

    return True


print(count_saddle(m, n))
