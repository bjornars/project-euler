import lib
import math

lim = 10000
primes = list(lib.get_primes(lim))[1:]
primes_s = set(primes)
double_squares = set(x*x*2 for x in range(int(math.sqrt(lim))))

found = False

for x in range(33, lim, 2):
    if x in primes_s:
        continue

    for p in primes:
        diff = x - p
        if diff <= 1:
            found = True
            print x
            break

        if diff in double_squares:
            break

    if found:
        break
