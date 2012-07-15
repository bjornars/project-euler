convert :: Char -> Integer
convert x = read [x]

fac 0 = 1
fac n = n * fac (n-1)

digits = show $ fac 100
answer = sum $ map convert digits

