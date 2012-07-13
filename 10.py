def get_primes(limit):
    numbers = [True] * limit
    numbers[0] = False
    numbers[1] = False

    for sieve in range(2, limit):
        if not numbers[sieve]:
            # find next prime
            continue

        yield sieve

        for x in range(sieve+sieve, limit, sieve):
            numbers[x] = False
        
print sum(get_primes(2000000))

