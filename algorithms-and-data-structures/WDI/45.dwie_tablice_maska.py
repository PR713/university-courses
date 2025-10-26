#########
def pierwsza(n):
    if n == 2 or n == 3: return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:  # i = 5,7,11,13,17,19,23,25,29...
        if n % i == 0: return False
        i += 2
        if n % i == 0: return False
        i += 4
    return True

# 0 - element z tablicy 1, 1 - element z tablicy 2, 2 - elementy z obu tablic
# system trójkowy: n % 3: [ 0, 1, 2 ]
def tworzenie_maski(t1, t2, mask):
    suma = 0
    for i in range(len(t1)): #bierze wszystkie indeksy po kolei
        if mask % 3 == 0:
            suma += t1[i]
            print(f' {t1[i]} ', end = '')
        if mask % 3 == 1:
            suma += t2[i]
            print(f' {t2[i]} ', end = '')
        if mask % 3 == 2:
            suma += t1[i] + t2[i]
            print(f' {t1[i]} + {t2[i]} ', end = '')
        if i < len(t1)-1: print('+', end = '')
        mask //= 3 #tutaj dopiero tworzymy maskę z kolejnych liczb
    print(' = ', suma)
    return suma

def maska_trójkowa(t1, t2):
    licznik = 0
    for mask in range(3 ** len(t1)):
        if pierwsza(tworzenie_maski(t1,t2,mask)): licznik += 1
    return licznik

t1 = [1, 3, 2, 4]
t2 = [9, 7, 4, 8]
print(maska_trójkowa(t1, t2))

