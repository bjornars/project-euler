from math import sqrt, floor
from lib import memoize

def pentagonal(n):
    return (n * (3 * n -1)) / 2

def is_pentagonal(n):
    s = sqrt(1+24*n)
    return s == floor(s) and int(s) % 6 == 5

f = False

for diff in range(1,1150):
    if f: break
    for k in range(1, 1500):
        j = diff + k
        p_k = pentagonal(k)
        p_j = pentagonal(j)

        if is_pentagonal(p_j - p_k) and is_pentagonal(p_j + p_k):
            print p_j - p_k
            f = True
            break
