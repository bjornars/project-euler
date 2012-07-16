def is_bouncy2(s):
    l = len(s) - 1
    for ix in range(0, l):
        if s[ix] > s[ix+1]: 
            for iy in range(0, l):
                if s[iy] < s[iy+1]: 
                    return True
    return False

bouncy = 0
bouncers = set()

x = 100
skip = 7
while True:
    X = str(x)
    for exp in range(skip, 1, -1):
        if X[:-exp] in bouncers:
            tens = 10**exp
            newx = x + tens
            newx = newx / (tens/10) * (tens/10)
            newb = bouncy + newx - x
            if newb * 100 >= newx * 99: # cant go over exactly 99%
                skip -= 1
                continue
            x = newx
            bouncy = newb
            bouncers.add(X)
            break
    else:
        if is_bouncy2(X):
            bouncy += 1
            bouncers.add(X)
        
        if bouncy * 100 == x * 99:
            print  x
            break
        x+= 1
