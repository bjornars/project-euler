import itertools
from lib import gcd

def is_equal_fraction(n1, d1, n2, d2):
    return n1 * d2 == n2 * d1

def rev(l):
    return list(reversed(l))

def is_curious(n, d):
    ns = map(int, str(n))
    ds = map(int, str(d))
    return ns[1] == ds[0] and is_equal_fraction(n, d, ns[0], ds[1])

total_n = 1
total_d = 1
for n in range(10, 100):
    for d in range(n+1, 100):
        if is_curious(n, d):
            total_n *= n
            total_d *= d

factor = gcd(total_n, total_d)

print "%d/%d" % (total_n/factor, total_d/factor)
