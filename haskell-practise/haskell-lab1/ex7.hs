not' :: Bool -> Bool
not' True = False
not' False = True

isItTheAnswer1 :: String -> Bool
isItTheAnswer1 _      = False
isItTheAnswer1 "Love" = True -- :)

isItTheAnswer2 :: String -> Bool
isItTheAnswer2 "Love" = True -- :)
isItTheAnswer2 _      = False -- to działa git to wyżej nie

or' :: (Bool, Bool) -> Bool
or' (True, _) = True
or' (_, True) = True
or' (_, _) = False

and' :: (Bool, Bool) -> Bool
and' (False, _) = False
and' (_, False) = False 
and' (_, _) = True -- szybciej (True, True) -> True, _ -> False

nand' :: (Bool, Bool) -> Bool
nand' (False, _) = True -- lub (True,True) = False
nand' (_, False) = True --      (_, _) = True
nand' (_, _) = False

