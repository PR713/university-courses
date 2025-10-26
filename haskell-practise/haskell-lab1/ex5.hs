sgn :: Int -> Int
sgn n = if n < 0
	then (-1)
	else if n == 0
		then 0
		else 1

absInt :: Int -> Int
absInt a = if a < 0 then -a else a 


min2Int :: (Int, Int) -> Int
min2Int (x,y) = if x < y then x else y





min3Int :: (Int, Int, Int) -> Int
min3Int (x,y,z) = if x < y && x < z then x
		  else if y < x && y < z then y
		  else z

min3withmin2Iin :: (Int, Int, Int) -> Int
min3withmin2Iin (x,y,z) = min2Int( min2Int(x,y),z)


toUpper :: Char -> Char
toUpper c = 
	if 'a' <= c && c <= 'z' then toEnum (fromEnum c - 32)  -- Zamiana na wielką literę
  else c
