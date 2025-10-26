sqr x = x^2
funcFactory n = case n of
	1 -> id
	2 -> sqr
	3 -> (^3)
	4 -> \x -> x^4
	5 -> intFunc
	_ -> const n
	where 
		intFunc x = x^5



expApproxUpTo :: Int -> Double -> Double
expApproxUpTo n x 
	| n >= 0 = sum [x^k / fromIntegral (factorial k) | k <- [0..n-1]]
	| otherwise = error "n must be less than 6"
	where 
		factorial 0 = 1
		factorial n = n * factorial (n - 1)

--lub prod' ...



dfr :: (Double -> Double) -> Double -> (Double -> Double)
dfr f h = \x0 -> (f (x0 + h) - f x0) / h



--dfr (\x -> x) 2.0 10
--lub let f' = dfr (\x -> x) 2.0, potem f' 10