array_sodoku = []

for i in range(9):
    item = list(map(int, input().split()))
    array_sodoku.append(item)


def check_sodoku(sodoku):
    row = 9
    col = 9

    for i in range(0, row, + 3):
        for j in range(0, col, + 3):
            numeric = [] * 9
            for ii in range(1, 10):
                numeric.append(ii)

            for k in range(3):
                for l in range(3):
                    if sodoku[i + k][j + l] not in numeric:
                        return False
                    else:
                        numeric.remove(sodoku[i + k][j + l])

    # check row
    for i in range(row):
        numeric = [] * 9
        for ii in range(1, 10):
            numeric.append(ii)

        for j in range(col):
            if sodoku[i][j] not in numeric:
                return False
            else:
                numeric.remove(sodoku[i][j])

    # check col
    for j in range(col):
        numeric = [] * 9
        for ii in range(1, 10):
            numeric.append(ii)

        for i in range(row):
            if sodoku[i][j] not in numeric:
                return False
            else:
                numeric.remove(sodoku[i][j])

    return True


if check_sodoku(array_sodoku):
    print("YES")
else:
    print("NO")
