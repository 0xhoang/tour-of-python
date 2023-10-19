a = int(input())


def is_prime(a):
    if a < 2:
        return False

    for i in range(2, a):
        if a % i == 0:
            return False

    return True


def prime_number_closest(a):
    if is_prime(a):
        return a

    below_closest = 0
    above_closest = 0

    temp = a
    while temp >= 2:
        temp -= 1
        if is_prime(temp):
            below_closest = temp
            break

    temp = a
    while True:
        temp += 1
        if is_prime(temp):
            above_closest = temp
            break

    if a - below_closest <= above_closest - a:
        return below_closest

    return above_closest


total = prime_number_closest(a)

print(total)
