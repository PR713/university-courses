-- product type example (one constructor)
data CartInt2DVec = MkCartInt2DVec Int Int -- konwencja: prefix 'Mk' dla konstruktora
--kwestia tego że zawsze Inty przyjmujemy
xCoord :: CartInt2DVec -> Int
xCoord (MkCartInt2DVec x _) = x

yCoord :: CartInt2DVec -> Int
yCoord (MkCartInt2DVec _ y) = y



data Cart2DVec' a = MkCart2DVec' a a
--dowolne typy
xCoord' :: Cart2DVec' a -> a
xCoord' (MkCart2DVec' x _) = x

yCoord' :: Cart2DVec' a -> a
yCoord' (MkCart2DVec' _ y) = y



data Cart2DVec'' a = MkCart2DVec'' {x::a, y::a}
--dowolne typy, rekord
--xCoord'' :: Cart2DVec'' a -> a
--xCoord'' (MkCart2DVec'' {x = xVal, y = _}) = xVal

--yCoord'' :: Cart2DVec'' a -> a
--yCoord'' (MkCart2DVec'' {y = yVal, x = _}) = yVal -- uwaga na kolejność x,y
--
