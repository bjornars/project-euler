import lib

def repend_length(d):
    for x in range(1, d+1):
        if 10**x % d == 1:
            return x
    assert False

repend_lengths = ((repend_length(x), x) for x in lib.get_primes(1000) if x > 10)
print max(repend_lengths)[1]
