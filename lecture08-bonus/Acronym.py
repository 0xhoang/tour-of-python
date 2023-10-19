s = input()


def search_acronym(s):
    rs = ''
    rs = rs + s[0]

    for i in range(len(s)):
        if s[i] == ' ':
            rs = rs + s[i + 1]

    return rs.upper()


rs = search_acronym(s)
print(rs)
