def nwd(a, b):
    while a * b != 0:  # wystarczy wyznaczyć x =nwd(a,b) i potem nwd(x,c)
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b

def nww(a,b):
    return (a*b)//nwd(a,b)

a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))
c = int(input('Podaj trzecią liczbę: '))

print(f'nwd to: {nwd(nwd(a,b),c)}')
print(f'nww to: {nww(nww(a,b),c)}')

