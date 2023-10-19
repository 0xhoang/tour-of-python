row = int(input())

for i in range(row):
    if i == 0:
        print('*' * row)
        continue

    if i == row - 1:
        print('*' * row)
    else:
        print('*' + ' ' * (row - 2) + '*')
