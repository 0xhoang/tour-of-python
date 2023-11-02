def checkPalindarome(s, index):
    length = len(s)

    # break point
    if index >= length // 2:
        return True

    # condition
    if s[index] == s[length - 1 - index]:
        return checkPalindarome(s, index + 1)
    else:
        return False


n = int(input())
s = input()
rs = checkPalindarome(s, 0)
if rs:
    print("YES")
else:
    print("NO")
