s = input()


def count_str(s):
    count = 0
    # a -> z
    for i in range(97, 123):
        if chr(i) in s:
            count += 1

    # A -> Z
    for i in range(65, 91):
        if chr(i) in s:
            count += 1

    return count


print(count_str(s))
