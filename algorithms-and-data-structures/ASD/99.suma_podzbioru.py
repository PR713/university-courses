#Suma podzbioru
#A[0],...,A[n-1] Naturalne, T naturalne
#Czy da się wybrać liczby sumujące się
#dokładnie do T

#Funkcja F(S, b) = T/F podciag elementow ze
#zbioru 0,...,b, ktorego suma jest rowna S
#rekurencyjny zapis
#F(suma,ind) = F(suma,ind-1) lub F(suma-A[ind],ind-1)
#F(0,x) = True
#F(A[0],0) = True

def subseries(A, T): # A - tablica, T - suma
    n = len(A)
    F = [ [ False for _ in range(n) ] for _ in range( T + 1 ) ]

    F[0][0] = True
    for b in range( n ):
        F[0][b] = True

    F[A[0]][0] = True #dla pierwszego elementu mamy sumę A[0]

    for b in range(1, n): #podzbiór
        for S in range(T + 1): #różne sumy
            F[S][b] = F[S][b-1] #ta sama suma ale podzbiór 0,...,b-1
            if S - A[b] >= 0:
                F[S][b] = F[S][b] or F[ S - A[b] ][ b - 1 ] #b-1 bo z tym elementem
                #tworzy sumę S
                #lub zapis |= inny zapis or
    return F[T][n-1]

A = [1,0,2,6,3,7]
print(subseries(A,4))