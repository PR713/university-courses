
from math import log10
def check_if_closer(w,k,wk,kk,move):
    return (w+move[0]-wk)**2 + (k+move[1]-kk)**2 < (w-wk)**2+(k-kk)**2

def zad19(T,w,k):
  n = len(T)
  end_corners = [(0,0),(0,n-1),(n-1,0),(n-1,n-1)]
  def rek(w,k,ec):
     n = len(T)
     wk = ec[0]
     kk = ec[1]
     if w == wk and k == kk:
        return True
     else:
        for e in [(1,0),(1,1),(0,1),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
            if -1 < w + e[0] < n and -1 < k +e[1] < n and check_if_closer(w,k,wk,kk,e):
                next_n = T[w + e[0]][k + e[1]]
                if T[w][k] % 10 < next_n//10**(int(log10(next_n))):
                    if rek(T,w+e[0],k+e[1],ec):
                        return True
        return False
  for ec in end_corners:
      if rek(w,k,ec):
          return True
  return False

