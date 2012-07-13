sum_of_squares = sum . map (^2) 
squares_of_sum = (^2) . sum 

diff n = squares_of_sum ns - sum_of_squares ns
    where ns = [1..n]

answer = diff 100
