not'' :: Bool -> Bool
not'' b = case b of
		True -> False
		False -> True

absInt' n = 
  case (n >= 0) of
	True -> n
	_ -> -n

and'' :: (Bool, Bool) -> Bool
and'' x = case x of
	(True, True) -> True
	_ -> False

nor'' :: (Bool, Bool) -> Bool -- ~(p v q ) True gdy oba False
nor'' x = case x of
	(False, False) -> True
	_ 	-> False
