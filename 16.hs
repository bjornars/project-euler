convert :: Char -> Integer
convert x = read [x]

digits = show $ 2^1000
answer = sum $ map convert digits

