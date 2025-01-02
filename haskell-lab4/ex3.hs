data BinIntTree = EmptyIntBT |
                  IntNodeBT Int BinIntTree BinIntTree

sumBinIntTree :: BinIntTree -> Int
sumBinIntTree EmptyIntBT = 0
sumBinIntTree (IntNodeBT n lt rt) = n + sumBinIntTree lt + sumBinIntTree rt

--np let tree = IntNodeBT 10 (IntNodeBT 5 EmptyIntBT EmptyIntBT) (IntNodeBT 15 EmptyIntBT EmptyIntBT)
--sumBinIntTree tree
--mamy więc 10 + sumBinIntTree (IntNodeBT 5 EmptyIntBT EmptyIntBT) + sumBinIntTree (IntNodeBT 15 EmptyIntBT EmptyIntBT)
--lt ma jakby zawsze typ i 3 dane Int BinIntTree BinIntTree lub puste EmptyIntBT
--
--
--
--


data BinTree a = EmptyBT |
                 NodeBT a (BinTree a) (BinTree a)

sumBinTree :: (Num a) => BinTree a -> a
sumBinTree EmptyBT = 0
sumBinTree (NodeBT n lt rt) = n + sumBinTree lt + sumBinTree rt









data Expr a = Lit a | -- literal/value a, e.g. Lit 2 = 2
              Add (Expr a) (Expr a)

eval :: Num a => Expr a -> a
eval (Lit n) = n
eval (Add e1 e2) = eval e1 + eval e2

show' :: Show a => Expr a -> String
show' (Lit n) = show n
show' (Add e1 e2) = "(" ++ show' e1 ++ "+" ++ show' e2 ++ ")"




depthOfBT :: BinTree a -> Int
depthOfBT EmptyBT = 0
depthOfBT (NodeBT _ lt rt) = 1 + max (depthOfBT lt) (depthOfBT rt)


flattenBTPreorder :: BinTree a -> [a]
flattenBTPreorder EmptyBT = []
flattenBTPreorder (NodeBT x lt rt) = [x] ++ flattenBTPreorder lt ++ flattenBRPreorder
--inorder ma ... ++ [x] ++ ..., postorder ... ++ ... ++ [x] 




mapBT :: (a -> b) -> BinTree a -> BintTree b
mapBT _ EmptyBT = EmptyBT
mapBT f (NodeBT x lt rt) = NodeBT (f x) (mapBT f lt) (mapBT f rt)



insert :: Ord a => a -> BinTree a -> BinTree a
insert x EmptyBT = NodeBT x EmptyBT EmptyBT
insert x (NodeBT y lt rt)
	| x < y = NodeBT y (insert x lt) rt
	| x > y = NodeBT y lt (insert x rt) 
	| otherwise = NodeBT y lt rt -- już istnieje taki element
--i rekurencyjnie wywołujemy wgłąb i potem wracamy wywołaniem wstecz
