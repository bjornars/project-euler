import math
pairs = (map(float, x.split(',')) for x in open("99.txt").readlines())
print max((x[1] * math.log(x[0]), i) for i, x in enumerate(pairs, 1))[1]
