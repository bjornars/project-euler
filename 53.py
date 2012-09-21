import lib

coeffs = (lib.choose(n, k) for n in range(1,101) for k in range(1, n+1))
print sum(1 for n in coeffs if n >= 1000000)
