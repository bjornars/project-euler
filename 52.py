from lib import *
from functools import *
from itertools import *
from operator import *

sort = compose(list, sorted)

def is_same(a, b):
    return sort(str(a)) == sort(str(b))

def is_same_n(*a):
    is_first = partial(is_same, a[0])
    return all(map(is_first, a[1:]))

assert not is_same(12, 13)
assert is_same(31, 13)
assert is_same_n(123, 132, 312)
assert not is_same_n(143, 132, 312)
assert not is_same_n(143, 134, 312)

def make_mult(n):
    def g(x):
        return list(x * y for y in range(1,n+1))
    return g

for x in imap(make_mult(6), count(1)):
    if is_same_n(*x):
        print x
        break
