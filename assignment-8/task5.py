number = int(input("Input n: "))

primes = []

if number > 1:
    for i in range(2, number):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

dividers = []
for j in primes:
    while True:
        if number % j == 0:
            number = number / j
            dividers.append(j)
        else:
            break

print(dividers)
