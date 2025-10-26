n = int(input('Liczba rozłożona na iloczyn o najmniejszej różnicy: '))
najm_roznica = 0
second = 1
szukane = 0

for first in range(n // 2 + 1):  #przypadek gdy jest pierwsza potem
    for k in range(first):
        second = first - k #w ten sposób zaczynamy od najmniejszej różnicy
        #print(first,second)
        if first * second == n:
            najm_roznica = abs(first - second) #pierwsza znaleziona jest najmniejszą zawsze
            print(f'Szukane liczby to: {first},{second}')
            print(f'Różnica to {najm_roznica}')
            quit(0) #całkowite wyjście a nie przerwanie obecnej pętli
