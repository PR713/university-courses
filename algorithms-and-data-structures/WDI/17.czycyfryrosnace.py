n = int(input('Podaj liczbę którą chcesz sprawdzić: '))
cyfra = 0
cyfra_1 = 0
while n > 0:
    cyfra = n%10
    n = n//10
    cyfra_1 = n%10
    if cyfra_1 < cyfra:
        continue
    else:
        print('Cyfry tej liczby nie tworzą ciągu rosnącego.')
        quit(0)

print('Cyfry tej liczby tworzą ciąg rosnący :)')

