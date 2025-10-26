
#Definicja funkcji: f(i, j) = minimalna suma odległości biurowców
#z pozycji X[0], . . . , X[i] do przydzielonych im działek,
#przy założeniu, że biurowiec z pozycji X[i] ma przydzieloną działkę
#z pozycji Y[j]. Rekurencja:
#f(i,j) = abs(X[i]-Y[j]) + min(f(i-1,j-1), f(i-1,j-2), ... ,f(i-1,i-1))
#f(0,a) = abs(X[0] - Y[a])
#Wynik min(f(n-1,j)), gdzie n-1 to indeks ostatniego biurowca, j >= n-1
#Algorytm działa w taki sposób, że wybieramy kolejno działki (pierwszy for),
#a następnie kolejno przebiegamy potencjalne parkingi dla danego biurowca,
#range(i,m), ponieważ wcześniejsze i-1 biurowców już musi mieć i-1
#przydzielonych parkingów. Aktualizujemy min_sum_prev, która przechowuje
#na bieżąco najmniejszą sumę odległości dla biurowców poprzednich gdzie
#parking ostatniego biurowca (i-1 go) ma indeks 'j-1'.

def parking(X, Y):
    n, m = len(X), len(Y)
    F = [[float('inf') for _ in range(m)] for _ in range(n)]

    for a in range(m):
        F[0][a] = abs(X[0] - Y[a])

    for i in range(1, n):  #kolejne biurowce
        min_sum_prev = float('inf')
        for j in range(i, m):  #kolejne potencjalne parkingi
            min_sum_prev = min(min_sum_prev, F[i - 1][j - 1])
            F[i][j] = min(F[i][j], abs(X[i] - Y[j]) + min_sum_prev)

    result = float('inf')
    for j in range(n-1,m):
        result = min(result, F[n-1][j])
    return result
#lub     return min(F[n-1][j] for j in range(n-1,m))