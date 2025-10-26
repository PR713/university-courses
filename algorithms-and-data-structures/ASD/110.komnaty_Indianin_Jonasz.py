#Radosław Szepielak
#A[y][x][i] - ile komnat można najwięcej odwiedzić wchodząc do komnaty
#(y,x) początkowo od lewej (pierwszy for zagnieżdżony), potem ewentualnie
#aktualizujemy czyli i = 1 wejście od góry, i = 0 wejście od dołu.
#wynik to max(A[n-1][n-1]) to ile najwięcej komnat można odwiedzić wchodząc do
#komnaty docelowej (n-1,n-1).

#rekurencja:
#A[x][y][i] = {max(A[y][x-1][0], A[y][x-1][1], A[y-1][x][i]) + 1, dla i = 1
#             {max(A[y][x-1][0], A[y][x-1][1], A[y+1][x][i]) + 1, dla i = 0
#A[a][0][1] = a (wejście od góry i = 1 o ile możliwe L[a][0] != '#')

#Za każdym razem przepisujemy do komnaty na prawo wartość max jaką można
#dojść do komnaty po lewej sąsiadującej. Następnie sprawdzamy od góry do
#dołu wartości z jakimi można wejść do komnat patrząc na poprzednie
#i aktualizujemy wynik. Analogicznie próbujemy iść od dołu do góry
#i aktualizujemy ewentualnie wynik, ponieważ do komnaty można wejść oprócz
#z lewej strony co robimy na samym początku również od góry, a także od dołu.


def maze(L):
    n = len(L)
    A = [[[-1, -1] for _ in range(n)] for _ in range(n)]
    # A[x][y][i] wchodząc do pola (x,y) od i = 0 dołu, i = 1 od góry
    for i in range(n):  # czyli warunki brzegowe dopóki możemy iść w dół
        if L[i][0] != '#':
            A[i][0][1] = i
        else:
            break

    for x in range(1, n):  # kolumna
        for y in range(n):  # po wierszach
            k = max(A[y][x - 1])  # z lewej wejście do (y,x)
            # i bierzemy max z (y,x-1) obojętnie jak było wejście do niego
            # bo po prostu potem zawsze i tak można rozważać w górę lub w dół
            # na polu (y,x) nie ważne jak się dostaliśmy do (y,x-1)
            if k != -1 and L[y][x] != '#':  # czyli do jakiegoś po lewej
                # można wejść i do (y,x) również
                A[y][x] = [k + 1, k + 1]

        for y in range(1, n):  # od góry
            if L[y][x] != '#' and A[y - 1][x][1] != -1:  # czyli można od góry wejść
                A[y][x][1] = max(A[y][x][1], A[y - 1][x][1] + 1)
        # max ((y,x) z wejścia od lewej albo -1, poprzedni (y-1,x) z lewej/góra)

        for y in range(n - 2, -1, -1):  # od dołu
            if L[y][x] != '#' and A[y + 1][x][0] != -1:
                # czyli jeśli można wejść na (y,x) oraz do tego niżej (y+1,x)
                # jakoś dojść nie ważne jak (czy z lewej czy jakiegoś niżej jeśli
                # nie jest na samym dole)
                A[y][x][0] = max(A[y][x][0], A[y + 1][x][0] + 1)
                # max ((y,x) z lewej lub -1, dla pola (y+1,x))
    return max(A[n - 1][n - 1])



