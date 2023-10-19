m, n = map(int, input().split())


def find_col_negative_matrix(m, n):
    matrix = []

    for i in range(m):
        input_row = list(map(int, input().split()))
        row = []
        for j in range(n):
            row.append(input_row[j])

        matrix.append(row)

    rs = []
    for i in range(n):
        count = 0
        for j in range(m):
            if matrix[j][i] < 0:
                count += 1

        if count == m:
            rs.append(i)
        else:
            continue

    return rs


rs = find_col_negative_matrix(m, n)

for i in range(len(rs)):
    print(rs[i], end=' ')
