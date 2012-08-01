def is_palindrome(x):
    while x:
        if x[0] != x[-1]:
            return False
        x = x[1:-1]
    return True

# not used
def to_binary(x):
    """ actually backwards, but doesn't matter """
    s = ""
    bb = {True: '1', False: '0'}
    while x:
        s += bb[x&1]
        x /= 2
    if not s:
        s = "0"
    return s

total = 0

for x in range(1,1000000, 2):
    b = bin(x)[2:]
    s = str(x)

    if is_palindrome(s) and is_palindrome(b):
        total += x

print total
