
def min_koszt(T,k):
    def f(T,k,w = 0,suma = 0):
        nonlocal minsuma
        n = len(T)
        if w == n-1:
            minsuma = min(minsuma,suma)
        else:
            if k!= 0: f(T,k-1,w+1,suma+T[w+1][k-1])
            if k!= n-1: f(T,k+1,w+1,suma+T[w+1][k+1])
            f(T,k,w+1,suma+T[w+1][k])

    minsuma = 10**100
    f(T,k,suma = T[0][k])
    return minsuma
