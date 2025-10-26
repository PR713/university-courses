# dla 2315 będą to 21, 35, 231, 315.
n = int(input('Podaj liczbę naturalną o niepowtarzających się cyfrach bez zera: '))
cyfra = 0
cyfra_bitowo = 0
liczba_binarnie = ''
ilosc_cyfr = 0
n1 = str(n) #żeby potem porównywać na stringach
szukane_liczby = ''
wynik = 0

while n > 0:
    cyfra_bitowo = n % 10
    n //= 10
    ilosc_cyfr += 1  # zliczamy ilu cyfrowa

for x in range(1,2**(ilosc_cyfr)):#np dla 4 cyfrowej max do 15 ma sprawdzać
    #bo to zajmuje 4 bity 1+2+4+8 maksymalnie
    while x > 0:
        cyfra = x % 2
        x //= 2
        liczba_binarnie += str(cyfra)#liczba_binarnie lustrzane odbicie, bo robimy znak += czyli znak = znak + str(cyfra) i doklejamy od przodu a trzeba by dać str(cyfra) + znak albo potem [::-1]
    print('kolejne liczby binarnie',liczba_binarnie)
    a = len(liczba_binarnie)
    for i in range(0,a):
        if liczba_binarnie[i] == '1':
            szukane_liczby += n1[i]

    wynik = int(szukane_liczby)
    szukane_liczby = ''
    liczba_binarnie = ''
    if wynik % 7 == 0:
        print(f'Z {n1} można otrzymać takie podzielne przez 7: {wynik}')
quit('<3 <3 <3')

