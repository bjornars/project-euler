import itertools
from lib import memoize

def add_(number, prefix):
    if number == 0:
        return prefix
    return int(str(prefix) + str(number))

@memoize
def square(term, row):
    if term == 0: return 1
    if row == 0:  return 2**(term-1)

    return 2 * square(term - 1, row) + square(term, row - 1)

def num2(left):
    total = square(left, 0)
    sign = -1
    for x in range(10, left+1, 10):
        print 'sqr', left -x, x/10
        total += sign * square(left-x, x / 10)
        sign *= -1
    return total

@memoize
def num3(left):
    if left == 0:
        return 1
    if left < 0:
        return 0

    return sum(num3(left - x) for x in range(1,10))

memo4  = [1]
def num4(left):
    while len(memo4) <= left:
        memo4.append(sum(memo4[-9:]))

    return memo4[-1]

def gen(acc, left, results, lim):
    gen.count += 1
    # print acc, left
    if left == 0:
        results.append( (acc, 1) )
        return

    if len(acc) == lim:
        results.append( (acc, num4(left)) )
        return

    # assert len(acc) < lim

    for x in range(min(9, left), 0, -1):
    #for x in range(1, min(10, left+1)):
        gen(acc + str(x), left - x, results, lim)

def make_sum(results, limit):
    total = 0
    for each, times in results:
        total += int(each) * times
    return total  % 10 ** limit

def do_gen(left, sig):
    results = []
    gen("", left, results, sig)
    return make_sum(results, sig)

results = []
import time
s = 0
for x in range(1,18):
    gen.count = 0
    then = time.time()
    t = do_gen(13**x, 4)
    now = time.time()
    s += t
    print 'calls', gen.count
    print x, s, "%.3fs" % (now - then)
print s
