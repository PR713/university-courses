
from math import log10

def zad18(T,w,k):
    n = len(T)
    if w == k == n - 1:
        return True
    else:
        flag = False
        for e in [(1,0),(1,1),(0,1)]:
            if w + e[0] < n and k +e[1] < n:
                next_n = T[w + e[0]][k + e[1]]
                if T[w][k] % 10 < next_n//10**(int(log10(next_n))):
                    flag = flag or zad18(T,w+e[0],k+e[1])
        return flag


