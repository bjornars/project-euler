def powerize(d, pow):
    total =0
    while d:
        total += (d % 10) ** pow
        d = d/10
    return total

total = 0
for x in range(2,1000000):
    if powerize(x, 5) == x:
        print x
        total += x

print 'total', total
