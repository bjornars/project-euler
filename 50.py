import lib
lim = 1000000

primes = list(lib.get_primes(lim))

max_prime = (0, 0, 0)
for idx, start in enumerate(primes):
    total = start

    for num, p in enumerate(primes[idx+1:]):
        if total >= lim:
            break
        if lib.is_prime(total):
            max_prime = max(max_prime, (num + 1, total, start))
        
        total += p

print max_prime
