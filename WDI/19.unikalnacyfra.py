n = int(input('Czy ostatnia cyfra jest unikalna? '))
cyfra_ostatnia = n % 10
cyfra = 0
n = n//10
while n > 0:
    cyfra = n % 10
    n = n // 10
    if cyfra_ostatnia == cyfra:
        print('Niestety nie jest zakończona unikalną cyfrą')
        quit(0)

print(f'Tak jest zakończona unikalną cyfrą: {cyfra_ostatnia}')

