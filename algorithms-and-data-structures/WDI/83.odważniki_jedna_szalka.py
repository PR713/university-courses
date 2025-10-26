
def zad7(T,m):
    def rek(T,m,i):
        n = len(T)
        if m == 0:
            return True
        if i >= n:
            return False
        return rek(T,m-T[i],i+1) or rek(T,m,i+1)#gdy 2 szalki to or rek(T,m+T[i],i)
    return rek(T,m,0)
