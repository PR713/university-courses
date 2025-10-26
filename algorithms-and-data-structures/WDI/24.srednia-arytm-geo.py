a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))

eps = 1e-12
while abs(a-b) > eps:
    A,B = (a*b)**(0.5), (a+b)/2
    a,b = A,B
    print(a,b)
print(A)
