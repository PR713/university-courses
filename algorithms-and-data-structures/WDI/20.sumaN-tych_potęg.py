n_1 = 0
for n in range(1,10000):
    n_1 = n #tworzymy kopię 'n' bo on się zmienia w trakcie do 0
    suma_N_tych_poteg = 0
    cyfra = 0
    cyfry = []
    ilosc_cyfr = 0
    while n > 0:
        cyfra = n % 10
        cyfry.append(cyfra) # dodajemy do listy cyfry liczby n
        n = n // 10
        ilosc_cyfr += 1
        #print(ilosc_cyfr)
    for cyferki in (cyfry):
        suma_N_tych_poteg += cyferki**ilosc_cyfr
        #print(suma_N_tych_poteg)
    if suma_N_tych_poteg == n_1:
        print(n_1)