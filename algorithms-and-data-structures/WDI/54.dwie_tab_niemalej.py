def funkcja(tab):
    n = len(tab)
    tab1 = [0]*(n*n)
    lider = [0]*n
    i = 0
    minus_indeks = 0
    while i < n * n:
        minus = 999999999999999
        for j in range(n):
            if lider[j] >= n:#wyznacza ile już wzięliśmy z danego wiersza
                continue #pomija warunki niżej i iteruje dalej
            #tzn liczba pod danym indeksem 'j' określa którą liczbę ma wziąć
            # z j-tego wiersza
            if minus > tab[j][lider[j]]:
                minus = tab[j][lider[j]]
                minus_indeks = j
        tab1[i] = minus #dopisujemy do nowej tablicy
        lider[minus_indeks] += 1#zwiększa ile wzięliśmy el. z wiersza
        i += 1 #^^ dzięki temu też wybieramy kolejne elementy z wierszy
    return tab1

tab = [[1, 26, 35],
       [4, 5, 6],
       [7, 8, 9]]
print(funkcja(tab))