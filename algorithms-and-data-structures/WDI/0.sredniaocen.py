oceny = []
ilosc = 0
suma = 0
i = int(input('Ile ocen: '))
for _ in range(i):
    ocena = int(input('Podaj ocene: '))
    oceny.append(ocena)
    suma += ocena
    ilosc += 1
print(f'Średnia ocen {oceny} to: {suma / ilosc}')
