sumWith g [] = 0
sumWith g (x:xs) = g x + sumWith g xs

prodWith g [] = 1
prodWith g (x:xs) = g x * prodWith g xs


sumWith' :: Num a => ( a -> a ) -> [a] -> a
sumWith' = go 0 
	where 
		go acc g [] = acc
		go acc g (x:xs) = go (g x + acc) g xs


prodWith' :: Num a => (a -> a) -> [a] -> a
prodWith' = go 1
	where
		go acc g [] = 1
		go acc g (x:xs) = go (g x * acc) g xs


foldr' :: (a -> b -> b) -> b -> [a] -> b
foldr' f z [] = z -- z wartość początkowa
foldr' f z (x:xs) = f x (foldr' f z xs) -- tutaj akumulator cały czas to z przekazywany głębiej w stos, cofając się obliczamy dopiero poprzednie wartości wywołań ile to wynosi dane 
--foldr' od czegoś itd cofamy
--(1 - (2 - (3 - (4 - (5 - 0))))
--dla foldr1 bierze jako z ostatnią wartość z tablicy i dla reszty stosuje funkcję f
--czyli z = 5, reszta [1,2,3,4] czyli równoważne z tym kiedy z = 0
--1 - ( 2 - (3 - (4 - 5)
sumWith'' g = foldr' (\x acc -> g x + acc) 0 
prodWith'' g = foldr (\x acc -> g x * acc) 1



foldl' :: (b -> a -> b) -> b -> [a] -> b
foldl' _ z []     = z
foldl' f z (x:xs) = foldl' f (f z x) xs -- tutaj z zmienia się w czasie z nowe = f z x itd i w kolejnych wywołaniach bierzemy kolejne 'x' z xs, z się zmienia więc potem wraca z wartością docelową bo co chwilę go aktualizowaliśmy
-- [1,2,3,4,5] i z = 0 mamy (((((0 - 5) - 4) - 3) - 2) - 1)
-- dla foldl1 mamy ((((1 - 5) - 4) - 3) - 2)
-- z to pierwsza wartość left
sumWith''' g = foldl' (\acc x -> g x + acc) 0 
prodWith''' g = foldl' (\acc x -> g x * acc) 1



------------------------
isSortedAsc :: Ord a => [a] -> Bool
isSortedAsc [] = True
isSortedAsc [x] = True
isSortedAsc (x:y:xs) 
	| x <= y = isSortedAsc (y:xs)
	| otherwise = False

--z wykorzystaniec zip lub zipWith
isSortedAsc' :: Ord a => [a] -> Bool
isSortedAsc' xs = all ( uncurry (<=)) (zip xs ( tail xs))

everySecond :: [t] -> [t]
everySecond xs = [ x | (x,i) <- zip xs [1..], odd i]
