from lib import gcd, get_primes
import sys

primes = list(get_primes(500))


def small_factor(d):
    # the answer cannot have a large prime in it, since that makes it
    # more resilient - so we can be fast and lazy
    f = []
    for x in primes:
        while d % x == 0:
            f.append(x)
            d /= x

    if not d == 1:
        # we found high factors
        return False
    else:
        return f


def cmp_frac((n1, d1), (n2, d2)):
    return cmp(n1 * d2, n2 * d1)


def reduce_frac((n, d)):
    g = gcd(n, d)
    return n / g, d / g


def totient(x):
    # this is where the magic happens
    factors = set(small_factor(x))
    num = 1
    denum = 1
    for factor in factors:
        num *= (factor - 1)
        denum *= factor
    return (x * num) / denum, x - 1

if __name__ == "__main__":
    best = (1, 1)
    lim = 15499, 94744

    print '%s %.3f%%' % (lim, (lim[0] * 100.0 / lim[1]))

    i = 1
    for prime in list(get_primes(100)):
        i *= prime
        for mult in range(1, prime):
            # try the cumulative product of primes, times some multiplier less than the top prime
            x = i * mult
            res = totient(x)
            if cmp_frac(res, best) < 0:
                if cmp_frac(res, lim) < 0:
                    print 'found! %s %s %.3f%%' % \
                            (x, reduce_frac(res), (res[0] * 100.0 / res[1])), small_factor(x)
                    sys.exit(0)

                best = res
                print 'new best! %s %s %.3f%%' % \
                    (x, reduce_frac(res), (res[0] * 100.0 / res[1])), small_factor(x)
