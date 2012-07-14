fac 0 = 1
fac n = n * fac (n-1)

n `choose` k = fac n `div` (fac k * fac (n-k))
