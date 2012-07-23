from lib import memoize

denoms = [1, 2, 5, 10, 20, 50, 100, 200]
denoms.reverse()

@memoize
def num_change(left, last):
    if left == 0: return 1
    return sum(num_change(left - d, d) for d in denoms if left >= d and last >= d)

print num_change(200, 200)
