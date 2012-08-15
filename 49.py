import lib

lib._prime_limit = 10000

for x in range(1001, 10000, 2):
    if not lib.is_prime(x):
        continue
    inc_limit = ((10000 - x) / 2)
    for inc in range(10, inc_limit, 2):
        seq = x + inc, x + inc + inc
        if lib.is_prime(seq[0]) and lib.is_prime(seq[1]):
            s1 = sorted(str(x))
            if s1 == sorted(str(seq[0])) and s1 == sorted(str(seq[1])):
                print "%d%d%d" % (x, x+inc, x+inc+inc)
