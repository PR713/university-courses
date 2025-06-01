
def is_prime(x):
    if x < 2: return False
    if x == 2 or x == 3: return True
    if x % 2 == 0 or x % 3 == 0: return False
    i = 5
    while i * i <= x:
        if x % i ==0: return False
        i += 2
        if x % i ==0: return False
        i += 4
    return True

def dziesietnie(T):
    n = len(T)
    res = 0
    for i in range(n):
        res += T[i]*2**(n-i-1)
    return res

def zad5(T):
    n = len(T)
    def rek(i,j,T):
        if j > n - 1:
            return False
        if j == n -1:
            if T[j-1] == 0 and j-i+1 != 2:#10 jest pierwsza, inne nie
                return False
            return is_prime(T[i:j+1])
        if is_prime(T[i:j+1]):
            return rek(j+1,j+2,T)#czy można tak pociąć, a nie wszystkie
        #więc tutaj już możemy iść dalej

        return rek(i,j+1,T)
    return rek(0,1,T) if len(T) > 1 else False