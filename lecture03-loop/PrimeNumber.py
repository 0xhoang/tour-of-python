prime_number = int(input())

is_prime = True

for i in range(2, prime_number):
    if prime_number % i == 0:
        is_prime = False
        break

if prime_number < 2:
    is_prime = False

if is_prime:
    print("YES")
else:
    print("NO")
