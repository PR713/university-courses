a = 1
b = 1
n = 100  # dowolna
liczba = int(input('Podaj liczbę do sprawdzenia:'))
while (a < n):
    if liczba == a*b:
        print(f'liczba jest iloczynem dwóch wyrazów {a},{b}')
        quit(0)
    c = a + b
    a = b
    b = c

print('Nie istnieją takie dwa kolejne wyrazy')
