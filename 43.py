import itertools

primes = [(17, 7), (13, 6), (11, 5), (7, 4)]
total = 0
for perm in itertools.permutations([1,2,3,4,5,6,7,8,9,0]):
    if perm[3] % 2 != 0:
        continue
    if (perm[4] + perm[2] + perm[3]) % 3 != 0:
        continue
    if perm[5] % 5 != 0:
        continue
    if perm[0]== 0: 
        break

    for factor, i in primes:
        num = perm[i] * 100 + perm[i+1] * 10 + perm[i+2]
        if num % factor != 0:
            break
    else:
        n = 0
        for x in perm:
            n *= 10
            n += x
        total += n

print total

