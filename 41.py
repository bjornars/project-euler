from lib import get_primes
import lib

max_prime = 0
for x in range(1, 8):
    s = map(str, range(1,x+1))
    for perm in lib.permute(s):
        prime = int(''.join(perm))
        if lib.is_prime(prime):
            max_prime = prime

print max_prime
# primes = get_primes(9876543)
# print len(list(primes))
