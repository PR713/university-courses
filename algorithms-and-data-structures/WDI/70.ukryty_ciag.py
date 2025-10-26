def check_sum(beg,end,T):
    if end >= len(T)-1:
        return False
    mult = T[end+1]/T[beg]
    for i in range(end-beg+1):# range(length) tak naprawdę
        if end + i + 1 >= len(T) or T[end+i+1]/T[beg+i] != mult:
            return False
    return True

def sequence(T):
    n = len(T)
    for beg in range(n):
        for length in range(n,2,-1):
            if check_sum(beg,beg+length-1,T):
                return beg,beg+length-1