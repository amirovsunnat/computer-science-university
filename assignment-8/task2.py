number = int(input("Input m: "))
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
else:
    print(number, "is not a prime number")

print("List of prime numbers up to", number, ":", primes)
