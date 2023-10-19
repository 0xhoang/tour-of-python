number = int(input())

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


total = 0
for i in range(1, number):
    if is_prime(i):
        total += i

print(total)
