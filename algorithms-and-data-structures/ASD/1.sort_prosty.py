
#zaimplementować sortowanie proste
#tu bąbelkowe
def sortuj(T):
    n = len(T)
    for i in range(n-1):
        pom = False
        for j in range(n-i-1):
            if T[j+1] < T[j]:#byłoby niestabilne jeśli <= i obraca np 3 i 3
                T[j+1], T[j] = T[j], T[j+1]
                pom = True
        if not pom:
            break
    return T

T = [4,2,1,7,4,5,2,1]
print(sortuj(T))