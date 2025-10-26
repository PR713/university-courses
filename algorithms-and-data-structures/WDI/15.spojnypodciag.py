S = int(input('Podaj jakiej sumy podciąg sprawdzić: '))
a = 1
b = 1
aktualna_suma = 0

while aktualna_suma < S:
    aktualna_suma += a
    a,b = b,a+b

if aktualna_suma == S:
        print('TAK istnieje taki podciąg :)')
else:
    a = 1
    b = 1
    while aktualna_suma > S:
        aktualna_suma -= a
        a,b = b,a+b
    if aktualna_suma == S:
            print('TAK istnieje taki podciąg :)')

######### gdy nie istnieje to szukamy najbliższego większego od danej sumy
#możnaby wszystko w for, albo while co na górze, ale tutaj można niżej komentarze zmienić :)
if aktualna_suma != S:
  while True:
    S+=1
    while aktualna_suma < S:
        aktualna_suma += a
        a, b = b, a + b

    if aktualna_suma == S:
        print(f'istnieje taki podciąg ale dla liczby {S} :)')
        quit(0)
    else:
        a = 1
        b = 1
        while aktualna_suma > S:
            aktualna_suma -= a
            a, b = b, a + b
        if aktualna_suma == S:
            print(f'istnieje taki podciąg ale dla liczby {S} :)')
            quit(0)



