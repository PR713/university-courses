myFun x = 2 * x

add2T :: Num a => (a,a) ->  a
add2T (x,y) = x + y

add2C :: Num a => a -> ( a -> a)
add2C x y = x + y

f :: Num a => (a -> a) -> a
f g = g 1 -- f(g) = g(1)

add3T :: Num a => (a,a,a) -> a
add3T (x,y,z) = x + y + z

add3C :: Num a => a -> (a -> (a -> a))
add3C x y z = x + y + z

curry2 :: ((a,b) -> c) -> a -> b -> c
curry2 f x y = f (x,y)
-- mamy f x y czyli ((a,b) -> c) -> a -> b
--natomiast zwracamy -> c bo f (x,y) ma typ c
-- czyli fakt że curry przyjmuje funkcję z krotką a zwraca
-- funkcję która przyjmuje osobno bo czytając: funkcja curry przyjmuje
--funkcję (a,b) -> c i zwraca funkcję przyjmującą a która
--wywołuje funkcję przyjmującą b i zwracającą c
-- inaczej ((a,b) -> c) -> (a -> (b -> c )



uncurry2 :: (a -> b -> c) -> (a,b) -> c
uncurry2 f (x,y) = f x y

curry3 :: ((a,b,c) -> d) -> a -> b -> c -> d
curry3 f a b c = f(a,b,c)

fiveToPower_ :: Integer -> Integer
fiveToPower_ = (5 ^)

_ToPower5 :: Num a => a -> a
_ToPower5 = (^ 5)

subtr5From_ :: Num a => a -> a
subtr5From_ = (- 5 +) -- np 10 - 5
-- a subtrNFrom5 to (2 -) 10 czyli 2 - 10

flip2 :: (a -> b -> c) -> b -> a -> c 
flip2 f b a = f a b