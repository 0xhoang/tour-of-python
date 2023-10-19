qty = int(input())


def count_str(s):
    s = s.lower()

    min = 1000
    char = ''
    for i in range(97, 123):
        count = 0
        for j in range(len(s)):
            if s[j] == chr(i):
                count += 1

        if count == 1:
            return chr(i)
        elif 0 < count < min:
            min = count
            char = chr(i)

    return char


rs = []
for i in range(qty):
    s = input()
    rs.append(count_str(s))

for i in range(qty):
    print(rs[i].upper())
