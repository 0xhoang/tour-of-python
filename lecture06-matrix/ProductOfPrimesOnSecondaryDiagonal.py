n = int(input())


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def count_prime_on_secondary_diagonal_matrix(n):
    total = 1
    for i in range(n):
        input_row = list(map(int, input().split()))
        for j in range(n):
            if j == n - i - 1:
                if is_prime(input_row[j]):
                    total *= input_row[j]

    return total % 1000003


print(count_prime_on_secondary_diagonal_matrix(n))
