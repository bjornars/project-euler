import lib

def cycle(x):
    x = str(x)
    for each in range(0, len(x)):
        yield int(x[each:]+ x[:each])

assert list(cycle(1235)) == [1235, 2351, 3512, 5123]

primes = set(lib.get_primes(1000000))
candidates = set(primes)
cyclical = set()

while candidates:
    c = list(cycle(candidates.pop()))
    for prime in c:
        if not prime in primes:
            break
    else:
        for x in c:
            cyclical.add(x)
            candidates.discard(x)

print len(cyclical)
