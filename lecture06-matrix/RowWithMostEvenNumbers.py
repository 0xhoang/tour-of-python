m, n = map(int, input().split())


def is_event(n):
    if n % 2 == 0:
        return True
    else:
        return False


def find_row_has_much_event_num(m, n):
    rs = []

    for i in range(m):
        input_row = list(map(int, input().split()))
        count = 0
        for j in range(n):
            if is_event(input_row[j]):
                count += 1

        rs.append(count)

    max = rs[0]
    index = 0
    for i in range(1, len(rs)):
        if rs[i] > max:
            max = rs[i]
            index = i

    return index


print(find_row_has_much_event_num(m, n))
