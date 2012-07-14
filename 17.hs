sound_out :: Integer -> String
sound_out 0 = "zero"
sound_out n = sound_out' (n `div` 1000) ((n `div` 100) `mod` 10) ((n `div` 10) `mod` 10)   (n  `mod` 10) 
sound_out' :: Integer -> Integer -> Integer -> Integer-> String

sound_out' 0 0 0 0 = ""
sound_out' 0 0 0 1 = "one"
sound_out' 0 0 0 2 = "two"
sound_out' 0 0 0 3 = "three"
sound_out' 0 0 0 4 = "four"
sound_out' 0 0 0 5 = "five"
sound_out' 0 0 0 6 = "six"
sound_out' 0 0 0 7 = "seven"
sound_out' 0 0 0 8 = "eight"
sound_out' 0 0 0 9 = "nine"
sound_out' 0 0 1 0 = "ten"
sound_out' 0 0 1 1 = "eleven"
sound_out' 0 0 1 2 = "twelve"
sound_out' 0 0 1 3 = "thirteen"
sound_out' 0 0 1 5 = "fifteen"
sound_out' 0 0 1 8 = "eighteen"
sound_out' 0 0 1 o = sound_out' 0 0 0 o ++ "teen"
sound_out' 0 0 2 o = "twenty" ++ sound_out' 0 0 0 o
sound_out' 0 0 3 o = "thirty" ++ sound_out' 0 0 0 o
sound_out' 0 0 4 o = "forty" ++ sound_out' 0 0 0 o
sound_out' 0 0 5 o = "fifty" ++ sound_out' 0 0 0 o
sound_out' 0 0 8 o = "eighty" ++ sound_out' 0 0 0 o
sound_out' 0 0 t o = sound_out' 0 0 0 t ++ "ty"  ++ sound_out' 0 0 0 o
sound_out' 0 h 0 0 = sound_out' 0 0 0 h ++ "hundred"
sound_out' 0 h t o = sound_out' 0 0 0 h ++ "hundredand" ++ sound_out' 0 0 t o
sound_out' m h t o = sound_out' 0 0 0 m ++ "thousand" ++ sound_out' 0 h t o

answer = sum $ map (length . sound_out) [1..1000]
