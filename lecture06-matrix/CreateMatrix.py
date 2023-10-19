m, n = map(int, input().split())
a, b, p = map(int, input().split())


def create_matrix(m, n, a, b, p):
    matrix = []

    row_fist = []
    row_fist.append(a)
    row_fist.append(b)

    for i in range(2, n):
        row_fist.append((row_fist[i - 1] + row_fist[i - 2]) % p)

    matrix.append(row_fist)

    for i in range(1, m):
        row = []
        for j in range(n):
            if j == 0:
                row.append((matrix[i - 1][n - 2] + matrix[i - 1][n - 1]) % p)
                continue
            elif j == 1:
                row.append((matrix[i - 1][n - 1] + row[j - 1]) % p)
                continue
            else:
                row.append((row[j - 1] + row[j - 2]) % p)

        matrix.append(row)

    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


create_matrix(m, n, a, b, p)
