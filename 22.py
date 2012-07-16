data = sorted(map(lambda x:x[1:-1], open("22.txt").read().split(',')))

def score(name):
    return sum( (ord(x) - ord('A')+1) for x in name)

print sum( (i*score(x) for i, x in enumerate(data, 1)) )
