isPalindrome :: [Char] -> Bool
isPalindrome s = s == reverse s -- isPalindrome "ABBA" = True


-- Zdefiniować funkcję getElemAtIdx wykorzystując funkcje poznane
--powyżej (np. drop , head , tail )

getElemAtIdx :: [a] -> Int -> a -- zwraca liczbę
getElemAtIdx list idx = head (drop idx list)


getElemAtIdxUncurry :: ([a], Int) -> a
getElemAtIdxUncurry (list, idx) = head (drop idx list)

getListIdx :: [a] -> Int -> [a] -- zwraca listę
getListIdx list idx = drop idx list



primes :: [Int]
primes = eratoSieve [2..]
 where
  eratoSieve :: [Int] -> [Int]
  eratoSieve (p : xs) = p : eratoSieve [x | x <- xs, x `mod` p /= 0]

isPrime :: Int -> Bool
isPrime n 
	| n < 2 = False
	| otherwise = [i | i <- takeWhile(\i -> i * i <= n) primes, n `mod` i == 0] == []

