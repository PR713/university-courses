
def system_trójkowy(a):
    ile_jedynek = 0
    ile_dwojek = 0
    while a > 0:
        if a % 3 == 0:
            a //= 3
        if a % 3 == 1:
            ile_jedynek += 1
            a //= 3
        if a % 3 == 2:
            ile_dwojek += 1
            a //= 3
    return ile_jedynek, ile_dwojek #jeśli True to ma usunąć

print(system_trójkowy(123))

#a żeby wypisywało w dowolnym systemie:
def system(a,sys):
    l = 1
    liczba = 0
    while a > 0:
        m = (a%sys)*l
        l *= 10
        liczba += m
        a //= sys

    return liczba

print(system(10,2))