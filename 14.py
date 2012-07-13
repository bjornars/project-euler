collatz_lengths = {}
def collatz(n):
    if n == 1:
        return 1

    if n in collatz_lengths:
        return collatz_lengths[n]
    
    if n % 2 == 0:
        next = n / 2
    else: 
        next = 3*n + 1

    collatz_lengths[n] = collatz(next) + 1
    return collatz_lengths[n]

max_val = 0
max_start = 0
for x in range(1,1000000):
    n = collatz(x)
    if n > max_val:
        max_val = n
        max_start = x
print "Max was %d with %d" % (max_start, max_val)
