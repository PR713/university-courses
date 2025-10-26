n = 2
cyfra_n = 0  # cyfry w liczbie 'n'
suma_cyfr = 0  # suma cyfr danego czynnika pierwszego
i = 2

while n < 1000:
    n1 = n
    n2 = n
    suma_cyfr_n = 0  # suma cyfr w liczbie 'n'
    suma_cyfr = 0
    while n > 0:
        cyfra_n = n % 10
        n //= 10
        suma_cyfr_n += cyfra_n  # suma cyfr liczby 'n'
    # dobrze^^^^^^^^
    n = n1  # wracamy wartość n z kopii n1
    suma_rozkladu = 0  # suma cyfr czynników pierwszych
    cyfra_wrozkladzie = 0  # cyfry w danym czynniku pierwszym
    i = 2
    while i*i <= n2:  # ROZKLAD NA CZYNNIKI PIERWSZE
         if n1 % i == 0:
            n1 //= i
            a = i
            while a > 0:
                cyfra_wrozkladzie = a % 10
                ###print('Kolejne cyfry czynnika', cyfra_wrozkladzie)
                a //= 10
                suma_cyfr += cyfra_wrozkladzie# suma danego czynnika w rozkladzie
            suma_rozkladu += suma_cyfr
            suma_cyfr = 0
         else:
            i += 1

    # end while
    #n1 > 1 to ostatni czynnik z rozkładu - jest on l. pierwszą skoro n!=1
    if n1 > 1 and n1 < n2:#n1 < n2 eliminuje liczby n które od początku
        suma_cyfr = 0 #są pierwsze, a liczba Smith'a ma być liczbą złożoną
        b = n1
        while b > 0:
            cyfra_wrozkladzie = b % 10
            ###print('Dalsze cyfry z n>1 czynnika', cyfra_wrozkladzie)
            b //= 10 #sumowanie ost. czynnika
            suma_cyfr += cyfra_wrozkladzie
        suma_rozkladu += suma_cyfr
        suma_cyfr = 0
    ###print('Przed if', suma_rozkladu, suma_cyfr_n)
    if suma_rozkladu == suma_cyfr_n:
        print(f'Szukana liczba Smitha to {n2}')

    n += 1
