
--newtype Box a = MkBox a deriving Show

--instance Functor Box where
--	fmap f (MkBox x) = MkBox (f x)

-- fmap (^2) (MkBox 3) to to samo co (^2) <$> (MkBox 3)
--

{-# LANGUAGE DeriveFunctor #-}
newtype Box a = MkBox a deriving (Show, Functor)
--automatycznie tworzy instancje





--data MyList a = EmptyList
--              | Cons a (MyList a) deriving Show

--instance Functor MyList where
--  fmap _ EmptyList    = EmptyList
--  fmap f (Cons x mxs) = Cons (f x) (fmap f mxs)


data MyList a = EmptyList | Cons a (MyList a) deriving (Show, Functor)





--data BinTree a = EmptyBT | NodeBT a (BinTree a) (BinTree a) deriving (Show)

--instance Functor BinTree where
--	fmap _ EmptyBT = EmptyBT
--	fmap f (NodeBT a left right) = NodeBT (f a) (fmap f left) (fmap f right) 


data BinTree a = EmptyBT | NodeBT a (BinTree a) (BinTree a) deriving (Show, Functor)
