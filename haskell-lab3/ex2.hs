--let f33 = ((\(x,y,z) -> sqrt(fromIntegral(x^2+y^2+z^2))) :: Integral a => (a,a,a) -> Float)


sum' :: Num a => [a] -> a
sum' [] = 0
sum' (x:xs) = x + sum' xs


sumsqrt :: Floating a => [a] -> a
sumsqrt [] = 0
sumsqrt (x:xs) = sqrt x + sumsqrt xs


sumWith :: Num a => (a -> a) -> [a] -> a
sumWith _ [] = 0
sumWith f (x:xs) = f x + sumWith f xs

sum = sumWith(\e -> e)
sumSqr = sumWith(\e -> e*e)
sumCube = sumWith(\e -> e*e*e)
sumAbs = sumWith(\e -> abs e)

--sumWith (\e -> e^5) [1..15]

listLength = sumWith(\e -> 1)

prod' :: Num a => [a] -> a
prod' [] = 1
prod' (x:xs) = x * prod' xs


prodWith :: Num a => (a -> a) -> [a] -> a
prodWith _ [] = 1
prodWith f (x:xs) = f x * prodWith f xs


-- np ghci> prodWith (\e -> e**(0.5)) [1,4]
-- 2.0




