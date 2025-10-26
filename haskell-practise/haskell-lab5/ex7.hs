--mając pure (\x y z -> x + y * z) <*> Just 1 <*> Just 2 <*> Just 3
-- pure opakowuje funkcję wyżej w kontekst Maybe = Nothing | Just a
-- więc mamy tak jakby 
-- Just (\x y z -> x + y * z) <*> Just 1 <*> Just 2 <*> Just 3
-- potem Just (\y z -> 1 + y * z) <*> Just 2 <*> Just 3 itd... :)
-- <*> :: f (a -> b) -> f a -> f b, f to struktura tutaj Just i zwraca strukture tego samego typu ale z wartościami typu b
--
-- ogólnie <*> przyjmuje strukturę z funkcjami np listę funkcji, tutaj Just z funkcją jak z lambdą i stosuje to do elementów po prawej stronie
--pure (\x y z -> (x,y,z)) <*> Just 1 <*> Just 2 <*> Just 3
--
--lub od razu funkcję przekazujemy <$> do Justów np (\x y z -> (x,y,z)) <$> Just 1 <*> Just 2 <*> Just 3
 -- lub np (+) <$> (fmap read) getLine <*> fmap read getLine
 -- te nawiasy (fmap read) getLine opcjonalne bo i tak fmap oczekuje funkcji read i struktury (input tutaj) i konwertuje
 -- wejście String -> a np "42" na 42
 --
 -- np (:) <*> (\x -> [x]) $ 2 przekazuje 2 do całego wyrażenia
 -- więc mamy listę [2] i (:) pobiera to 2 przekazane i listę [2] i wstawia na początek czyli [2,2]
 --
 -- np (+) <$> (^2) <*> (^3) $ 3 bo <$> to inaczej fmap czyli mapuje funkcję ^2 na funkcję potem dodającą wartość
 -- czyli mapujemy, mamy ((^2) z +) czyli funckję f = \x -> (+) (x^2) zatem mamy: f <*> (^3) $ 3 i z zasługą <*> mamy
 -- finalnie g = \x -> (x^2) + (x^3) z przekazaniem 3 do tego przez $ :)
 --
 -- a fmap przyjmuje tylko jedną funkcję a nie strukturę z funkcjami :)
 







newtype Box a = MkBox a deriving Show

instance Applicative Box where
  pure = MkBox
  (MkBox f) <*> w = fmap f w

instance Functor Box where
	fmap f (MkBox x) = MkBox (f x)




