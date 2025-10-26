#REKURENCYJNIE
"""def silnia(n):
      if n == 0 or n == 1:
         return 1
      return n*silnia(n-1)

liczba_eulera = 0
for i in range(10):
    e = 1/silnia(i)
    liczba_eulera += e
print(liczba_eulera)"""
#### lub bez obliczania silni za każdym razem

#import decimal
#n = int(input('Z jaką precyzją po przecinku chcesz liczbę Eulera? '))
#decimal.getcontext().prec = n+1
EPS = 1e-10
def wyznacz_e():
    e = 2
    fact = 1 #Dla kazdego kolejnego wyrazu przemnazamy obliczona silnie (zmienna fact)
    i = 2
    while True:
        fact *= i
        i += 1
        next_elem = 1 / fact # decimal.Decimal(1) / decimal.Decimal(fact)
        if next_elem < EPS: #lub do tablicy dopisywać kolejne ułamki i potem zsumować.
            break
        e += next_elem
    return e

print(wyznacz_e())

