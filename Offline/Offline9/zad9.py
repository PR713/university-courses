#Radosław Szepielak
#Tworzę tablicę, która przechowuje na każdym indeksie 3 elementy,
#kolejno: wysokość pola (y,x) z tablicy M[y][x], indeks y, indeks x.
#Następnie sortuję rosnąco tablicę po wartościach A[i][0], aby potem
#w takiej kolejności wykonywać algorytm dynamiczny, ponieważ można tylko
#iść do pól o większej wartości, więc będzie to zawsze optymalne podejście.
#F(i,j) = dojście do pola (i,j) w maksymalnej liczbie kroków
#(po rosnących wysokościach)
#F[a][b] = max(F[a-1][b], F[a][b-1], F[a+1][b], F[a][b+1])
#Wynik max(F[i])
#Złożoność czasowa O(mnlog(mn)), pamięciowa O(mn)
from zad9testy import runtests

def trip(M):
    n = len(M[0])  # kolumny
    m = len(M)  # wiersze
    a = n * m
    A = [0] * (n * m)
    ind = 0
    for x in range(n):
        for y in range(m):
            A[ind] = (M[y][x], y, x)  # wysokość, wspołrzędne (i,j)
            ind += 1

    A = sorted(A, key=lambda d: d[0])  # posortowana po wartościach M[i][j]
    F = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(a):  # po tablicy A
        a, b = A[i][1], A[i][2]
        # czyli mamy jakieś współrzędne i,j
        if a + 1 < m and M[a][b] < M[a + 1][b]:
            F[a+1][b] = max(F[a+1][b], F[a][b] + 1)

        if b + 1 < n and M[a][b] < M[a][b + 1]:
            F[a][b+1] = max(F[a][b+1], F[a][b] + 1)

        if a - 1 >= 0 and M[a][b] < M[a - 1][b]:
            F[a-1][b] = max(F[a-1][b], F[a][b] + 1)

        if b - 1 >= 0 and M[a][b] < M[a][b - 1]:
            F[a][b-1] = max(F[a][b-1], F[a][b] + 1)
    maxi = 1
    for z in range(m):
        maxi = max(maxi,max(F[z]))
    return maxi

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(trip, all_tests=True)
