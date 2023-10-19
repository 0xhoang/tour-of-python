s = input()


def capital_letters(s):
    for i in range(len(s)):
        if s[i] == ".":
            if i != len(s) - 1 and s[i + 1] == " ":
                s = s[:i] + ". " + s[i + 2].upper() + s[i + 3:]

    return s


print(capital_letters(s))
