def Twin_Primes(n, m):
    l = []
    primes = []
    for i in range(n, m + 1):
        temp = []
        for j in range(2, i + 1):
            if i % j == 0:
                temp.append(j)
        if len(temp) == 1:
            primes.append(i)

    for prime in primes:
        t = ()
        for next_prime in primes:
            if next_prime - prime == 2:
                t = (prime, next_prime)
                l.append(t)


    return l