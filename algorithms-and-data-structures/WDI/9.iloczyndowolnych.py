a = 1
b = 1
n = 100  # dowolna
Fibonacci = []
while (a < n):
    c = a + b
    a = b
    b = c
    Fibonacci.append(a)

liczba = int(input('Podaj liczbę do sprawdzenia:'))
for j in (Fibonacci):
    for k in (Fibonacci):
        #print(j, k)
        if liczba == j * k and j < k:
            print(f'liczba jest iloczynem dwóch wyrazów {j},{k}')
            quit(0) #jeśli sprawdzimy wszystkie j i k, można dać też exit(0), przerywa obie pętle

print('Nie istnieją takie wyrazy')
