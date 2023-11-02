s = input()


def findFirstRepeatingChar(s):
    index_i = -1
    index_j = -1
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                if index_i == -1 and index_j == -1:
                    index_i = i
                    index_j = j
                elif index_j > j:
                    index_i = i
                    index_j = j

    if index_i >= 0:
        return s[index_i]

    return "null"


print(findFirstRepeatingChar(s))
