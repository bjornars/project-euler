fibs = {0: 1, 1:1, 2:1}
def fib(n):

    if n in fibs: return fibs[n]
    r =  fib(n-1) + fib(n-2)
    fibs[n] = r
    return r

import itertools
target = 10**999

for each in itertools.count():
    if fib(each) >= target:
        print each
        break
