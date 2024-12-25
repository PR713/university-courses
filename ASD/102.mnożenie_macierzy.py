
#ciąg macierzy a0xa1 * a1xa2 * a2*a3...
#(A[1]*A[2])*((A[3]*(A[4]*A[5]))*A[6])
#znaleźć nawiasowanie
#F(i,j) to minimalna liczba operacji dla wymnożenia
#podciągu od A_i do A_j -tej macierzy

def matrices_mul_cost(A):
    if len(A) < 2: return 0

    n = len(A)
    F = [[float('inf')] * n for _ in range(n)]

    for i in range(n): #reszta to zera
        F[i][i] = 0

    for i in range(n - 1):
        F[i][i + 1] = A[i][0] * A[i][1] * A[i + 1][1] #nad przekątną

    for j in range(2, n): #długości ciągów macierzy np j = 3, A2*A3*A4
        for i in range(n - j): #początki ciągów macierzy o długości j
            for k in range(i, i + j): #k wyznacza punkty podziału tego ciągu
            #od i do k, oraz k+1 do i+j-1, a dodajemy dodatkowo mnożenie tej
            #ostatniej i+j - tej macierzy, tzn mamy wtedy dwie jakieś macierze
            #jedna o wymiarze A[i][0]xA[k][1], druga A[k][1]xA[i+j][1]
                F[i][i + j] = min(F[i][i + j],
                                  F[i][k] + F[k + 1][i + j] + A[i][0] * A[k][1] * A[i + j][1])

    print(*F, sep='\n')

    return F[0][n - 1]

