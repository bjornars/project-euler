import lib
from operator import *
from functools import partial
from itertools import ifilter, imap

limit = 6
lim = 10**(limit)
llim = 10**(limit - 1)
target = 8
lt_llim = partial(lt, llim)

def get_mask(digit):
    def mask_out(t):
        x, y = t
        if x == '0':
            return y
        else:
            return '0'

    for x in range(1, 2**limit-1):
        mask = "0" * limit + bin(x)[2:]
        mask = mask[-limit:]
        masked = reduce(concat, lib.zipWith(mask_out, mask, str(digit)))
        yield map(int, (mask, masked))

def get_primes_streak(start):
    hits = []
    for mask, masked in get_mask(start):
        primes = filter(lib.is_prime, filter(lt_llim, (masked + mask * x for x in range(10))))
        if len(primes) >= target:
            return primes[0]
    return False

for x in ifilter(lt_llim, lib.get_primes(lim)):
    s = get_primes_streak(x)
    if s:
        print s
        break
