funcList :: [ Double -> Double ]
funcList = [ \x -> sin x / x
           , \x -> log x + sqrt x + 1
           , \x -> (exp 1) ** x ]
evalFuncListAt :: a -> [a -> b] -> [b]
evalFuncListAt x [] = []
evalFuncListAt x (f:fs) = f x : evalFuncListAt  x fs

--ghci> evalFuncListAt 2 funcList
--[0.45464871341284085,3.1073607429330403,7.3890560989306495]

--evalFuncListAt (-3) [id, abs, const 5, \y -> 2 * y + 8 ]



displEqs :: (Double -> Double, Double -> Double)
displEqs = (\t -> 4 * t^2 + 2 * t, \t -> 3 * t^2)

--let (x_t, y_t) = (fst displEqs, snd displEqs)
-- x_t 1 zwraca 1 el. z krotki displEqs z t = 1
--displEqs to krotka mająca dwie funkcje



dfc :: (Double -> Double) -> Double -> Double -> Double
dfc f h t = (f (t + h) - f t) / h

d2c :: (Double -> Double) -> Double -> Double -> Double
d2c f h t = (dfc f h (t + h) - dfc f h t) / h


velocEqs :: Double -> Double -> (Double, Double)
velocEqs h t = (dfc (fst displEqs) h t, dfc (snd displEqs) h t)
 
--velocEqs 0.01 1

accelEqs :: Double -> Double -> (Double, Double)
accelEqs h t = (d2c (fst displEqs) h t, d2c (snd displEqs) h t)


--np velocEqs 0.01 1 to około (10, 6)
-- veloc Eqs 0.01 2 to około (18, 12)
--bo accelEqs 0.01 1,2,... to (8, 6)
--'na jednostkę x czyli 1' wzrost o 6 f' (veloc),
--veloc wzrost o 12 funkcji f o x = 1 na lewo lub prawo

 
