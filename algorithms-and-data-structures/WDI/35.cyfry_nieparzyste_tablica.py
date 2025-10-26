tab = [2, 4, 16, 18, 37, 38]
for i in range(len(tab)):
    cnt = 0
    cnt_cyfr = 0
    liczby = tab[i]
    cyfra = 0
    while liczby > 0:
        cyfra = liczby % 10
        if cyfra % 2 != 0:
            cnt += 1
        else:#break jeśli choć jedna nieparysta, szybsze
            break
        liczby //= 10
        cnt_cyfr += 1  # zlicza ile cyfr ma liczba
    if cnt > 0 and cnt_cyfr == cnt:
        print(f'Tak, na przykład {tab[i]} ma tylko cyfry nieparzyste')
        quit(0)