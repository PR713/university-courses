
def rook(N,L):
    n = N
    def rek(N,L,w=0,k=0,cnt=0):
        mini=float("inf")
        if w == k == n-1:
            return cnt
        else:
            for y in range(w+1,n):#wiersz
                if (y,k) in L:
                    break
                mini = min(mini, rek(N, L, w + y, k, cnt + 1))

            for x in range(k+1,n):#kolumna
                if (w,x) in L:
                    break
                mini = min(mini,rek(N,L,w,k+x,cnt+1))
        return mini

    mini = rek(N,L)
    return mini if mini != float("inf") else None

L = [(0,2),(1,1)]#,(2,0)]
print(rook(3,L))
