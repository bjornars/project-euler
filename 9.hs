triplet = [(a, b, c) |
            a <-[1..999],
            b <- [a..999],
            c <- [1000 - a - b],
            a*a + b*b == c*c]

product' (a, b, c) = a * b * c
answer = product' $ head triplet
