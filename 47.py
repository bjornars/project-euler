import lib
import itertools

@lib.memoize
def len_fac(n):
    return len(set(lib.factors(n)))

def get(num):
    x = 2
    while True:
        for e in range(num):
            if not len_fac(x + e) == num:
                x += e + 1
                break
        else:
            return x

print get(2)
print get(3)
print get(4)

