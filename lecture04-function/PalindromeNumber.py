a = int(input())


def is_palindrome(a):
    digit = 0
    temp = a
    while temp > 0:
        temp = temp // 10
        digit += 1

    digit -= 1

    temp = a
    while a > 0:
        last = a % 10
        a = a // 10

        last1 = temp // (10 ** digit)
        temp = temp % (10 ** digit)

        digit -= 1

        if last != last1:
            return False

    return True


if is_palindrome(a):
    print("YES")
else:
    print("NO")
