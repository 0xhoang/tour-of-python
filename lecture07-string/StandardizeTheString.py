s = input()


def standardize_string(s):
    while True:
        if len(s) == 0:
            break

        if s[0] == ' ':
            s = s[1:]
        else:
            break

    while True:
        if len(s) == 0:
            break

        if s[-1] == ' ':
            s = s[:-1]
        else:
            break

    while True:
        if len(s) == 0:
            break

        if '  ' in s:
            s = s.replace('  ', ' ')
        else:
            break

    return s

print(standardize_string(s))
