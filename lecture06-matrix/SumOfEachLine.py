m, n = map(int, input().split())


def sum_matrix(m, n):
    rs = []
    for i in range(m):
        row = list(map(int, input().split()))
        sum = 0
        for j in range(n):
            sum += row[j]

        rs.append(sum)

    for ii in range(len(rs)):
        print("{0}: {1}".format(ii, rs[ii]))


sum_matrix(m, n)
