#Radosław Szepielak
#F(i,j,k) = maksymalna suma z zakresu zaczynającego się na i, koniec na j
#z pominięciem co najwyżej k elementów. Iteruję przez tablicę T,
#i oznacza początek zakresu, j koniec zakresu, a oznacza maksymalną liczbę
#liczb jaką można usunąć z tego fragmentu. Sortuję następnie ten zakres
#i kolejno pomijam następne wartości od najmniejszych z tego zakresu posortowanego,
#w ten sposób maksymalizując sumę w zakresnie [i,j] z pominięciem k elementów.
#F(i,j,k) = max( F(i,j,k), F(i,j,k-1) + minA)
#Złożoność czasowa O(n^3 logn)
#Złożoność pamięciowa O(n)


from egz1btesty import runtests


def kstrong(T, k):
    n = len(T)
    F = [[ [-float('inf') for _ in range(k+1)] for _ in range(n)] for _ in range(n)]
    suma = [0] * n
    suma[n-1] = T[n-1]
    for j in range(n-1,0,-1):
        suma[j-1] = suma[j] + T[j-1]

    for a in range(n):
        F[a][n-1][0] = suma[a]
    for b in range(n):
        F[b][b][0] = T[b]
        F[b][b][1] = 0

    for i in range(n):
        for j in range(i,n):
            A = T[i:j+1]
            A.sort()
            cnt = 0

            for a in range(1,k+1): #bo k jest O(n)

                if cnt >= j-i+1: break
                minA = A[cnt]
                if minA < 0: minA = -minA

                F[i][j][a] = max(F[i][j][a], F[i][j][a-1] + minA )
                cnt += 1
    ans = 0
    for i in range(n):
        for j in range(n):
            for a in range(k+1):
                ans = max(ans, F[i][j][a])
    return ans


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kstrong, all_tests=True)
