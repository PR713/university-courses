import Data.Char
import Data.List

capitalize :: [Char] -> [Char]
capitalize [] = [] 
capitalize (x:xs) = toUpper x : (map toLower xs)

formatStr s = foldr1 (\w s -> w ++ " " ++ s) . map capitalize . filter (\x -> length x > 1) $ words s
--po prostu wybiera o length > 1, capitalizację robi, foldr1 więc bierze dla
--"tomasz t   , bogdan anna . Jerzy j     maria"
--bierze Tomasz ++ Bodan ++ Anna ++ Jerzy ++ Maria, Maria to akumulator przekazywany głęboko dalej
--Tomasz Bogdan Anna Jerzy dla nich mamy f x ( foldr1 f z xs), Maria na końcu i przed nią x ++ Maria..

--a dla foldl1 akumulator Tomasz, potem mamy Tomasz ++ Bogdan i oni są akumulatorem już bo
--z nowe = f z x
--
--
--
--




prodPrices p = case p of
	"A" -> 100
	"B" -> 500
	"C" -> 1000
	_ -> error "Unknown product"

products = ["A", "B", "C"]

--basic discount strategy
discStr1 p
	| price > 999 = 0.3 * price
	| otherwise = 0.1 * price
	where price = prodPrices p

--flat discount strategy
discStr2 p = 0.2 * prodPrices p 
totalDiscount discStr = 
	foldl1 (+) . map discStr . filter (\p -> prodPrices p > 499
--po prostu filtruje i dodaje te > 499 po odpowiedniej funkcji mapuje i dodaje po kolei,
--foldr1 też by dodawał tak samo tylko że najpierw np x potem y + x, potem z + y + x cofając się rekurencją, bo f x (fold f z xs),
--foldl ma foldl f (f z x) xs i na bieżąco oblicza i wchodzi głębiej po liście,
--jeśli foldl1 to acc to pierwszy, dla foldr1 to ostatni
