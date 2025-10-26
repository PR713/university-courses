wyraz1 = 0
wyraz_ciagu = 0
licznik_kroków = 0
licznik_największy = 0
a = 0
for a1 in range(2,10001):#założenie
    licznik_kroków = 0
    wyraz_ciagu = 0
    wyraz1 = a1
    while wyraz_ciagu != 1:
       wyraz_ciagu = (wyraz1%2) * (3*wyraz1 + 1)+(1 - wyraz1%2) * wyraz1/2
       wyraz1 = wyraz_ciagu
       #print(wyraz_ciagu)
       licznik_kroków += 1
    #print(f'Licznik dla {a1} to: {licznik_kroków}')
    if licznik_kroków > licznik_największy:
        licznik_największy = licznik_kroków
        a = a1
print(f'Największa liczba kroków dla {a} to {licznik_największy} ')

