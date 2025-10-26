
def bin(x):
    jedynki = 0
    while x > 0:
        if x % 2 == 1:
            jedynki += 1
        x //= 2
    return jedynki

def zad28(T,org=1,ile1=0,ile2=0,ile3=0,indeks=0):
    n = len(T)
    if org:
        org = 0
        for i in range(n):
            T[i] = bin(T[i])

    if indeks == n:
        return True if ile1 == ile2 == ile3 else False

    return zad28(T,0,ile1+T[indeks],ile2,ile3,indeks+1) or\
           zad28(T,0,ile1,ile2+T[indeks],ile3,indeks+1) or\
           zad28(T,0,ile1,ile2,ile3+T[indeks],indeks+1)

T = [5,7,15]
print(zad28(T))