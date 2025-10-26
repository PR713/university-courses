from egz3btesty import runtests


def uncool1(P):
    n = len(P)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            a,b = P[i]
            c,d = P[j] # b < c or d < a to rozłączne, reszta zawieranie
            if not (b < c or d < a or (a >= c and b <= d) or (c >= a and d <= b)):
                return (i,j)
        #nie można robić inaczej bo więcej przypadków
        #np [2,10], [10,12]

def uncool1( P ):
    n = len(P)
    for i in range(n):
        a, b = P[i]
        P[i] = (a, b, i)
    P.sort(key=lambda x: (x[0], x[1]))
    left = 0
    right = 1
    while right < n:
        while P[left][1] < P[right][0] and left < right:
            left += 1 #wyklucza że będą rozłączne, ale nadal mogą
            #na siebie nachodzić
        a, b, k = P[left]
        c, d, l = P[right]
        if a < c < b < d: #wyklucza że będą się zwierać
            return k, l

        right += 1 #czyli nie spełniają warunków => zawierają się

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool1, all_tests = True )


"""
def findBinFirst(tab,el,indeks):
    p=0
    k=len(tab)-1
    while p<=k:
        s=(p+k)//2
        if tab[s][indeks]<el:
            p=s+1
        else:
            k=s-1
    if p<len(tab) and el==tab[p][indeks]:
        return p
    return -1
def find(T,x):
    n=len(T)
    i=-1
    k=-1
    for j in range(n):
        if T[j]==x:
            i=j
        elif  (T[j][0]<x[0] and x[0]<T[j][1]<x[1]) or (x[1]>T[j][0]>x[0] and T[j][1]>x[1]):
            k=j
        if i>-1 and k>-1:
            return i,k
    return -1,-1
           
 
def uncool( P ):
    n=len(P)
    pa=sorted(P,key=lambda x:x[0])
    pb=sorted(P,key=lambda x:x[1])
    for i in range(n):
        start=findBinFirst(pa,pa[i][0]+1,0)
        end=findBinFirst(pa,pa[i][1],0)
        sa=end-start
        finA=findBinFirst(pb,pa[i][1]+1,1)
        startB=findBinFirst(pa,pa[i][0]+1,0)
        dom=finA-startB
        dom=dom if dom>=0 else 0
        if sa > dom :
          #print(pa[i],'p')
          a,b=find(P,pa[i])
          if a>-1 and b>-1:
           return a,b
         
        start=findBinFirst(pa,pa[i][0]+1,1)
        end=findBinFirst(pa,pa[i][1],1)
        sa=end-start
        if sa > dom:
            #print(pa[i],'k')
            a,b=find(P,pa[i])
            if a>-1 and b>-1:
             
              return a,b
           
    return -1,-1"""
