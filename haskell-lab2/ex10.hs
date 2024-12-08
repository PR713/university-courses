fst2Eq :: Eq a => [a] -> Bool
fst2Eq (x : y : _) | x == y = True
fst2Eq _                    = False


fstmodsec :: Integral a => [a] -> Bool
fstmodsec (x : y : _) | y `mod` x == 0 = True
fstmodsec _ = False

