products :: [Integer]
products = [x * y | x <- [999,998..100], y <- [x,x-1..100]]

is_palindrome x = x' == reverse x'
               where x' = show x

biggest_palindrome = maximum $ filter is_palindrome $ products
