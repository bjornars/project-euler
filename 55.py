def lychr(a):
    a = str(a)
    return int(a) + int(a[::-1].lstrip('0'))

def is_palindrome(a):
    a = str(a)
    return a == a[::-1]

# could exploit some symmetries to improve the performance, but it finishes in ~0.2 seconds anyways
def try_lychr(a):
    for x in range(1,51):
        a = lychr(a)
        if is_palindrome(a):
            return x

    return False

assert lychr(124) == 545
assert lychr(120) == 141
assert try_lychr(196) == False
assert try_lychr(47) == 1
assert try_lychr(349) == 3

print sum(1 for x in range(1,10000) if not try_lychr(x))

