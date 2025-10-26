import Data.Char (toLower)
doubleElems [] = []
doubleElems (x:xs) = 2 * x : doubleElems xs


map' :: ( a -> b ) -> [a] -> [b]
map' _ [] = []
map' f (x:xs) = f x : map f xs

doubleElems1 = map' (*2)
sqrElems1 = map' sqrt
lowerCase = map' toLower


doubleElems2 :: Num a => [a] -> [a]
doubleElems2 xs = [2 * x | x <- xs]


--length . filter even $ doubleElems [1..10^7] --działa wolno bo doubleElems wolno działa
--length . filter even $ map' (*2) [1..10^7] -- 5 razy szybciej bo 
--
--ghci> map (map length) [ [[1], [1,2] , [1,2,3]], [[1], [1,2]] ]               [[1,2,3],[1,2]]
--(0.01 secs, 63,480 bytes)
--ghci> map length [ [[1], [1,2] , [1,2,3]], [[1], [1,2]] ]
--[3,2]
--(0.01 secs, 55,232 bytes)
--ghci> map (map length) [ [[1], [1,2] , [1,2,3]], [[1], [1,2]]]
--[[1,2,3],[1,2]]
--muszą mieć zgodne typy np [[Int]] i [[Int]] a nie [[Int]] i [Int]


