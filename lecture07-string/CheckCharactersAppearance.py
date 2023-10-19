s = input()


def check_charactors(s):
    str = s.upper()

    for i in range(len(str)):
        if str[i] == "B" or str[i] == "I" or str[i] == "G" or str[i] == "O":
            return "YES"

    return "NO"


print(check_charactors(s))