import itertools
import lib

# n^2 + an + b
def num_euler(a, b):
    for n in itertools.count():
        if not lib.is_prime(n*n + a*n + b):
            return n

if __name__ == '__main__':
    assert num_euler(1, 41) == 40
    assert num_euler(-79, 1601) == 80

    max_coef = None
    max_num = -1
    for a, b in itertools.product(range(-999, 1000, 2), lib.get_primes(1000)):
        n = num_euler(a,b)
        if n > max_num:
            max_num = n
            max_coef = (a,b)

    print max_coef
