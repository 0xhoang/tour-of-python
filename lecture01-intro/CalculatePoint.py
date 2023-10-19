n = int(input())

digit1 = n % 10

n = int(n / 10)
digit2 = n % 10

n = int(n / 10)
digit3 = n % 10

n = int(n / 10)
digit4 = n % 10

n = int(n / 10)
digit5 = n % 10

total = digit1 + digit2 + digit3 + digit4 + digit5
print(total % 10)
