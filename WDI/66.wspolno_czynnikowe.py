def wsp_czyn(a, b):#też co do ilości wystąpienia czynnika
    cnt = 0
    i = 2
    while a != 1 and b != 1:
       cnt_a = 0
       while a%i ==0:
           a //= i
           cnt_a += 1

       cnt_b = 0
       while b%i ==0:
           b//=i
           cnt_b += 1

       cnt += min(cnt_a, cnt_b)
       i += 1
       if cnt > 1:
           return False
    return cnt == 1

def four(T):
    n = len(T)
    cnt = 0
    for i in range(1,n-1):
        for j in range(1,n-1):
            if wsp_czyn(T[i][j],T[i-1][j]) and wsp_czyn(T[i][j],T[i+1][j]) and\
            wsp_czyn(T[i][j],T[i][j-1]) and wsp_czyn(T[i][j],T[i][j+1]):
                cnt += 1
    return cnt

