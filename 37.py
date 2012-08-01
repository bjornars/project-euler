import lib
primes = lib.get_primes(1000000)
primes = set(map(str, primes))

def is_trunc(c):
    c2 = c[1:]
    for each in "2", "4", "6", "8", "0":
        if each in c2:
            return False
    x = c
    while x:
        if not x in primes:
            return False
        x = x[1:]

    x = c
    while x:
        if not x in primes:
            return False
        x = x[:-1]

    return True

total = 0
for x in primes:
    if is_trunc(x) and int(x) > 10:
        total += int(x)
print total
