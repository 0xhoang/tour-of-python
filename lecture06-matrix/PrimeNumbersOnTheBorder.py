m, n = map(int, input().split())


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def count_prime_in_matrix(m, n):
    total = 0
    for i in range(m):
        input_row = list(map(int, input().split()))
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                if is_prime(input_row[j]):
                    total += 1

    return total


print(count_prime_in_matrix(m, n))
