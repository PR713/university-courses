def odd(a):
    return a % 2 == 1

def palindrom(T,a,b):
    n = len(T)
    i = 0
    cnt = 0
    while b + i < n and a - i >= 0:
        if not T[a-i] == T[b+i]:
            return cnt
        if odd(T[a-i]) and odd(T[b+i]):#zatem muszą być równe i nieparzyste: True and True
          cnt += 2
          i += 1
        else: return cnt
    return cnt

def dlugosc_podciagu(T):
    n = len(T)
    maxi = 0
    for i in range(1,n-1):
        if odd(T[i]):
            if odd(T[i+1]) and T[i] == T[i+1]:
                maxi = max(maxi,palindrom(T,i,i+1)) # np [1,3,3,1]
            maxi = max(maxi,palindrom(T,i-1,i+1) + 1) #np [1,3,5,7,5,3,1]
    return maxi