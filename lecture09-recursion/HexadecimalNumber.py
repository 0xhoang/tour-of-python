n = int(input())


def convert_hexadecimal(n):
    if n > 16:
        convert_hexadecimal(n // 16)

    num = n % 16

    if num == 10:
        print("A", end='')
    elif num == 11:
        print("B", end='')
    elif num == 12:
        print("C", end='')
    elif num == 13:
        print("D", end='')
    elif num == 14:
        print("E", end='')
    elif num == 15:
        print("F", end='')
    else:
        print(num, end='')


rs = convert_hexadecimal(n)
