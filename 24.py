import lib

def make_perm(digits, perm_nr):
    if len(digits) == 1:
        return [digits[0]]

    f = lib.factorial(len(digits)-1)
    n = perm_nr / f
    return [digits.pop(n)] + make_perm(digits, perm_nr % f)

print "".join(map(str, make_perm(list(range(10)), 999999)))
