from lib import divisors
from itertools import product

def is_abundant(n):
    # print divisors
    return sum(divisors(n)) > n

assert is_abundant(196)

limit = 24000

abu = set()
for x in range(1, limit):
    if is_abundant(x):
        abu.add(x)

abu = list(sorted(abu))

numbs = set()
for x in abu:
    for y in abu:
        if x  < y: break
        numbs.add(x+y)

numbs = set(range(1,limit)).difference(numbs)
print len(numbs), sum(numbs)
