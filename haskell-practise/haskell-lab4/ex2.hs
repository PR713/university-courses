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








-- sum type example (two constructors)
data List a = EmptyL | Cons a (List a) deriving Show

head' :: List a -> a
head' EmptyL 	= error "head': the empty list has no head!"
head' (Cons x xs) = x 





-- enum type example (special case of sum type)
data ThreeColors = Blue |
                   White |
                   Red

type ActorName = String

leadingActor :: ThreeColors -> ActorName
leadingActor Blue  = "Juliette Binoche"
leadingActor White = "Zbigniew Zamachowski"
leadingActor Red   = "Irene Jacob"








-- Definicja typu
data Cart3DVec a = MkCart3DVec a a a

-- Funkcje dostępowe
xCoord3D :: Cart3DVec a -> a
xCoord3D (MkCart3DVec x _ _) = x

yCoord3D :: Cart3DVec a -> a
yCoord3D (MkCart3DVec _ y _) = y

zCoord3D :: Cart3DVec a -> a
zCoord3D (MkCart3DVec _ _ z) = z


--Definicja bez Mk
data Cart3DVec' a = Cart3DVec' a a a
-- Funkcje dostępowe
xCoord3D' :: Cart3DVec' a -> a
xCoord3D' (Cart3DVec' x _ _) = x

yCoord3D' :: Cart3DVec' a -> a
yCoord3D' (Cart3DVec' _ y _) = y

zCoord3D' :: Cart3DVec' a -> a
zCoord3D' (Cart3DVec' _ _ z) = z




--record syntax
data Cart3DVecRec a = Cart3DVecRec
  { xCoord3D'' :: a
  , yCoord3D'' :: a
  , zCoord3D'' :: a
  } deriving Show






-- pole
data Shape = Circle Float  -- Konstruktor koła z promieniem
           | Rectangle Float Float -- Konstruktor prostokąta

area :: Shape -> Float
area (Circle r) = pi * r * r  -- Wzór na pole koła
area (Rectangle a b) = a * b  -- Wzór na pole prostokąta




