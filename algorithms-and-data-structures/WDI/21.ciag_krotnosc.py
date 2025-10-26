a = int(input('Podaj liczbę - czy wielokrotność jakiegoś wyrazu ciągu jest jej równa? '))
wyraz_ciagu = 0
wielokrotnosc_wyrazu = 0
ile_takich_wyrazów = 0
i = 0
while wyraz_ciagu < a:  # tyle wyrazów ciągu wyznaczamy
    i += 1
    wyraz_ciagu = i * i + i + 1
    print(wyraz_ciagu)
    for k in range(1, a // 2 + 1):#pierwszy to 3 więc spokojnie wystarczy, nawet a//3 +1
        wielokrotnosc_wyrazu = k * wyraz_ciagu
        if wielokrotnosc_wyrazu == a:
            print(f'Liczba {a} to wielokrotność {i}-ego wyrazu: {k}*{wyraz_ciagu} = {wielokrotnosc_wyrazu}')
            ile_takich_wyrazów += 1

if ile_takich_wyrazów == 0:
    print('Nie istnieje taki wyraz ciagu :(')
