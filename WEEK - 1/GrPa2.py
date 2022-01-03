def Goldbach(n):
    l = []
    primes = []
    for i in range(2, n + 1):
        temp = []
        for j in range(2, i + 1):
            if i % j == 0:
                temp.append(j)
        if len(temp) == 1:
            primes.append(i)
    for prime in primes:
        for next_prime in primes:
            if prime + next_prime == n:
                if prime <= next_prime:
                    t = (prime, next_prime)
                    l.append(t)

    return l
n = int(input())
print(sorted(Goldbach(n)))
