from math import sqrt

def hexagonal(n):
    return n * (2*n-1)

def is_square(n):
    sq = int(sqrt(n))
    return sq * sq == n

def get_triangular(n):
    return (-1 + sqrt(1+8*n)) / 2

def is_pentagonal(n):
    return is_square(1+24*n) and int(sqrt(1+24*n)) % 6 == 5

import itertools

for x in itertools.count(143):
    n = hexagonal(x)
    if is_pentagonal(n):
        print get_triangular(n), n
        break
