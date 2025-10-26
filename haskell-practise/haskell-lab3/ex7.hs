import Data.Char (isUpper)
onlyEven [] = []
onlyEven (x:xs)
	| x `mod` 2 == 0 = x : onlyEven xs
	| otherwise 	= onlyEven xs


filter' :: ( a -> Bool ) -> [a] -> [a]
filter' _ [] = []
filter' p (x:xs)
	| p x = x : filter' p xs
	| otherwise     = filter' p xs

onlyEven1 = filter' even
onlyOdd = filter' odd
onlyUpper = filter' isUpper


