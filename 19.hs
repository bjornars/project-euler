daysPerMonth month
        | m `elem` [0, 2, 4, 6, 7, 9, 11]     = 31
        | m `elem` [3,5,8,10]                 = 30
        | y `mod` 400 == 0                    = 29
        | y `mod` 100 == 0                    = 28
        | y `mod` 4 == 0                      = 29
        | otherwise                           = 28
        where m = month `mod` 12
              y = 1900 + month `div` 12

-- get cumulative days since 1-1-1900 for all months from 1901-1 to 1999-12
cumulDays = drop 12 $ scanl (+) 0 $ map daysPerMonth [0..(12*101)-1]

isSunday d = d `mod` 7 == 6
answer = length $ filter isSunday cumulDays
