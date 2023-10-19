qty = int(input())


def standardize_name(s):
    s = s.lower()

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

    for i in range(len(s)):
        if s[i] == ' ':
            s = s[:i] + " " + s[i + 1].upper() + s[i + 2:]
        elif s[i].isdigit():
            s = s[:i] + s[i + 1:]

    if len(s) > 0:
        s = s[0].upper() + s[1:]

    return s


rs = []
for i in range(qty):
    s = input()
    rs.append(standardize_name(s))

for i in range(qty):
    print(rs[i])
