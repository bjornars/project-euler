from math import sqrt

def num_sol(n):
    sol = 0
    max_cat = int(n/(2 + sqrt(2)))
    for a in range(1, max_cat + 1):
        bc = n -a
        b = (bc - a*a/bc) / 2
        c = bc - b
        if a <=b and a*a + b*b == c * c:
            sol += 1
    return sol

max_sol = (0, 0)

for x in range(1,1001):
    n = num_sol(x)
    max_sol = max(max_sol, (n, x))

print max_sol[1]
