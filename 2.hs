fib = (map fib' [0..] !!)
    where fib' 1 = 1
          fib' 2 = 1
          fib' n = fib (n-2) + fib (n-1)

fibs = fibs' 1 1

-- this is what we want, endless stream
fibs' :: Integer -> Integer -> [Integer]
fibs' n n' = n:rest
       where rest = fibs' n' (n + n')

sum_of_even_below n = sum $ filter (\x -> mod x 2 == 0) $ takeWhile (<n) fibs

answer = sum_of_even_below 4000000
