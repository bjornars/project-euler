def get_divisors(x):
    if x < 10:
        l = 4
    elif x < 100:
        l = 3
    elif x < 1000:
        l = 2
    else:
        l = 1

    d1 = 10 ** (l) / 2
    d2 = 10 ** (l - 1)
    return d1, d2

def pan_length(x, y):
    return len("%s%s%s" % (x, y, x*y))

def is_pan(*args):
    p = set(range(1,10))
    for a in args:
        while a:
            x = a % 10
            if not x in p:
                return False
            p.remove(x)
            a /= 10
    return not p

products = set()
for x in range(1,9999):
    d1, d2 = get_divisors(x)
    for y in range(d2, d1):
        if is_pan(x, y, x*y):
            print x, y, x*y
            products.add(x*y)

print sum(products)
