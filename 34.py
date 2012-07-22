from lib import factorial

facs = {}
for x in range(10):
    facs[str(x)] = factorial(x)

def is_curious(n):
    return sum(map(facs.get, str(n))) == n

total = 0
for x in range(10, facs["9"]*7):
    if is_curious(x):
        total += x
print total
