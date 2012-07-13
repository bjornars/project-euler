gcd' :: Integer -> Integer -> Integer
gcd' 0 m = m
gcd' n 0 = n
gcd' n m 
    | n < m     =  gcd' n (m `mod` n)
    | otherwise =  gcd' m (n `mod` m)

lcd' :: Integer -> Integer -> Integer
lcd' n m = n*m `div` gcd' n m

lcdN = foldr1 lcd'

answer = lcdN [1..20]
