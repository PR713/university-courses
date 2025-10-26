def king(N,L):
    def rek(N,L,y,x,cnt,prev):
        maxi = 0
        if y == N-1 and x == N-1:
            return cnt
        if x < N-1 and (y,x+1) not in L:
            maxi = max(maxi,rek(N,L,y,x+1,cnt+1,None))
        if y < N-1 and (y+1,x) not in L:
            if prev!= "up":
              maxi = max(maxi,rek(N,L,y+1,x,cnt+1,"down"))
        if y > 0  and (y-1,x) not in L:
            if prev != "down":
              maxi = max(maxi,rek(N,L,y-1,x,cnt+1,"up"))
        return maxi
    return(rek(N,L,0,0,0,None))


