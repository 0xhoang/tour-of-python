n = int(input())


def count_queen(n):
    matrix = []

    for i in range(n):
        input_row = list(map(int, input().split()))
        row = []
        for j in range(n):
            row.append(input_row[j])

        matrix.append(row)

    count_queen = 0
    for i in range(n):
        for j in range(n):
            if check_queen(matrix, n, i, j):
                count_queen += 1

    return count_queen


def check_queen(matrix, n, row, col):
    is_queen = True

    max_num_of_row = matrix[row][col]
    # check max row
    for j in range(n):
        if matrix[row][j] > max_num_of_row:
            is_queen = False
            break

    if is_queen == False:
        return False

    # check max col
    for j in range(n):
        if matrix[j][col] > max_num_of_row:
            is_queen = False
            break

    if is_queen == False:
        return False

    # check main diagonal

    # above main diagonal
    above_row = row
    above_col = col
    while above_row >= 0 and above_col >= 0:
        if matrix[above_row][above_col] > max_num_of_row:
            is_queen = False
            break

        above_row -= 1
        above_col -= 1

    if is_queen == False:
        return False

    # below main diagonal

    above_row = row
    above_col = col
    while above_row < n and above_col < n:
        if matrix[above_row][above_col] > max_num_of_row:
            is_queen = False
            break

        above_row += 1
        above_col += 1

    if is_queen == False:
        return False

    # check second diagonal

    # above second diagonal
    above_row = row
    above_col = col

    while above_row >= 0 and above_col < n:

        if matrix[above_row][above_col] > max_num_of_row:
            is_queen = False
            break

        above_row -= 1
        above_col += 1

    if is_queen == False:
        return False

    # below second diagonal
    above_row = row
    above_col = col
    while above_row < n and above_col >= 0:

        if matrix[above_row][above_col] > max_num_of_row:
            is_queen = False
            break

        above_row += 1
        above_col -= 1

    if is_queen == False:
        return False

    return True


print(count_queen(n))
