numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is_prime = True
primes = []
not_primes = []
for i in range(2, len(numbers)):
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
    is_prime = True
print("Primes:", primes)
print("Not Primes:", not_primes)
