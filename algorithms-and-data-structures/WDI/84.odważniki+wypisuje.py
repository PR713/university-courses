
def zad9(T,m):
    def rek(T,m,i,chosen):
        n = len(T)
        if m == 0:
            print(chosen)
            return True
        if i >= n:
            return False
        return rek(T,m-T[i],i+1,chosen+[T[i]]) or rek(T,m,i+1,chosen) or rek(T,m+T[i],i+1,chosen+[T[i]])
    return rek(T,m,0,[])

T = [2,3,7,2]
print(zad9(T,6))