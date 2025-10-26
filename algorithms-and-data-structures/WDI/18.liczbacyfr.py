n = int(input('Czy występuje cyfra równa liczbie cyfr tej liczby? '))
n_1 = n
ilosc_cyfr = 0
cyfra = 0
while n > 0:
    cyfra = n % 10
    n = n // 10
    ilosc_cyfr += 1 #lub sufit z log_10 (n)

while n_1 > 0:
    cyfra = n_1 % 10
    n_1 = n_1 // 10
    if cyfra == ilosc_cyfr:
        print(f'Tak istnieje, jest to cyfra: {cyfra}')
        quit(0)

print('Nie istnieje taka cyfra :(')