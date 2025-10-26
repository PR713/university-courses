# Zadanie 3. (ładowanie promu)
# Dana jest tablica A[n] z długościami samochodów, które stoją
# w kolejce, żeby wjechać na prom. Prom ma dwa pasy (lewy
# i prawy), oba długości L. Proszę napisać program, który wyznacza,
# które samochody powinny pojechać na który pas, żeby na promie
# zmieściło się jak najwięcej aut. Auta muszą wjeżdżac w takiej
# kolejności, w jakiej są podane w tablicy A

def pasy(A, i, d1, d2, C, car):
    if d1 < 0 or d2 < 0:
        C.pop()
        return (len(C) - 1, C) #bo o jeden mniej jak długość przekroczona
    if d1 == 0 and d2 == 0:
        return (len(C), C)
    if i >= len(A):
        return (len(C), C)
    w1, c1 = pasy(A, i + 1, d1 - car, d2, C + [(car, 1)], A[i + 1])
    w2, c2 = pasy(A, i + 1, d1, d2 - car, C + [(car, 2)], A[i + 1])
	#po skończeniu wywołania (już ma przypisane coś z 3 ifów wyżej)
    if w1 > w2: #liczba samochodów if na lewym > na prawym
        return (w1, c1)
    else:
        return (w2, c2)


C = []
L = 10
A = []
rozklad = pasy(A, 0, L, L, C, A[0])
