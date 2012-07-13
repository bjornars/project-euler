has_zero_remainder :: Int -> Int -> Bool
has_zero_remainder div num = div `mod` num == 0

is_multiple_of :: [Int] -> Int -> Bool
is_multiple_of list n = or $ map (\d -> n `mod` d == 0) list

sum_below :: Int -> Int
sum_below x = sum $ filter (is_multiple_of [3,5]) [1..(x-1)]

answer = sum_below 1000
