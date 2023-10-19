n = int(input())


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def count_prime_on_main_diagonal_matrix(n):
    total = 0
    for i in range(n):
        input_row = list(map(int, input().split()))
        for j in range(n):
            if i == j:
                if is_prime(input_row[j]):
                    total += 1

    return total


print(count_prime_on_main_diagonal_matrix(n))
