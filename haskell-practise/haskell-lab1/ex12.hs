f (x, y, z) = 
    if x == 3 then
        case (y > 2, z) of
            (True, False) -> x
            _ -> x + 2
    else
        x + y
