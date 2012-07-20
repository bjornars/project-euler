# count the number of rising numbers
up_memo = {}
def gen_up(last, n):
    if n == 1:
        if last == 0:
            last = 1
        return 10 - last

    n -= 1

    sum = 0

    k = n * 10 + last
    if k in up_memo:
        return up_memo.get(k)

    for each in range(last, 10):
        g = gen_up(each, n)
        sum += g

    up_memo[k] = sum
    return sum

# count the number of decreasing numbers
down_memo = {}
def gen_down(last, n):
    if n == 1:
        if last == -1:
            last = 9
        return last + 1

    n -= 1

    sum = 0
    if last == -1:
        stop = 10
    else:
        stop = last + 1

    k = str(last) + str(n)
    if k in down_memo:
        return down_memo.get(k)

    for each in range(0, stop):
        if last == -1 and each == 0:
            each = -1
        sum += gen_down(each, n)

    down_memo[k] = sum

    return sum

# total of rising and decreasing numbers, removing 0 and duplicates
def non_bouncy(n):
    up = gen_up(0, n)
    down = gen_down(-1, n) - 1
    total  = up + down - (n *9)
    return total

import time

then = time.time()
b = non_bouncy(100)
now = time.time()
print "%8d - %.3f seconds" % (b, now - then)
