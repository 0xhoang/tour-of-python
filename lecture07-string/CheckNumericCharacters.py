s = input()


def count_numberics(s):
    count = 0
    for i in range(len(s)):
        if s[i].isdigit():
            count += 1

    return count

print(count_numberics(s))