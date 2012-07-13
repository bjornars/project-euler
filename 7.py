def get_primes():
    primes = []
    num = 1
    while 1:
        num += 1
        for factor in primes:
            if num % factor == 0:
                break
        else:
            primes.append(num)
            yield num

print zip(get_primes(), range(10001))[-1]
