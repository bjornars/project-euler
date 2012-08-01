def nlen(args):
    return sum(map(len, args))

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

answer = 0
for start in range(1,99999):
    prods = []
    prods.append(str(start))
    for y in range(2,10):
        prods.append(str(start*y))
        l = sum(map(len, prods))
        if l == 9:
            pan = "".join(prods)
            if is_pan(int(pan)):
                answer = max(answer, int(pan))
            break
        elif l > 9:
            break

print answer        
