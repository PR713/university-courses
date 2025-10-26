#Dana jest szachownica A o wymiarach n×n. Szachownica
# zawiera liczby wymierne. Należy przejść z pola (1,1) na pole
#(n,n)korzystając jedynie z ruchów „w dół” oraz „w prawo”.
#Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba.
#Proszę podać algorytm znajdujący trasę o minimalnym koszcie.

#F(x,y) = min( F(x-1,y)+A[x][y], F(x,y-1)+A[x][y])
#               W      dół lub w prawo
#F(i,j) minimalny koszt jakim dotarto do (i,j) z (0,0)
def chessboard_rec(A):#top-down rekurencja
    N = len(A)
    DP = [[float('inf')]*N for i in range(N)]
    DP[0][0] = A[0][0]
    #oraz DP[i][0] i DP[0][i]
    for i in range(1,N):
        DP[i][0] = DP[i-1][0] + A[i][0]
        DP[0][i] = DP[0][i-1] + A[0][i] #bo wiemy jaki jest koszt dotarcia

    def F(i, j, N):
        if DP[i][j] != float('inf'):
            return DP[i][j]
        if i - 1 >= 0:
            DP[i - 1][j] = F(i - 1, j, N)  # spamiętanie
        if j - 1 >= 0:
            DP[i][j - 1] = F(i, j - 1, N)  # spamiętanie (rekurencja)
        return min(A[i][j] + DP[i - 1][j], A[i][j] + DP[i][j - 1])
    return F(N-1,N-1,N)

"""
def F(i, j):
        if DP[i][j] != float('inf'):
            return DP[i][j]
        if i > 0:
            DP[i][j] = min(DP[i][j], A[i][j] + F(i - 1, j))
        if j > 0:
            DP[i][j] = min(DP[i][j], A[i][j] + F(i, j - 1))
        return DP[i][j]
    return F(N-1,N-1)
"""



########## iteracyjnie

def chessboard_iter(A): #bottom-up iteracyjnie
    n = len(A)
    DP = [[float('inf')]*n for i in range(n)]
    DP[0][0] = A[0][0]
    #oraz DP[i][0] i DP[0][i]
    for i in range(1,n):
        DP[i][0] = DP[i-1][0] + A[i][0]
        DP[0][i] = DP[0][i-1] + A[0][i] #bo wiemy jaki jest koszt dotarcia

    for i in range(1,n):
        for j in range(1,n):
            DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + A[i][j]
    return DP[n-1][n-1]

A = [[1,4,2,6,1],
     [0,2,1,5,2],
     [2,7,3,1,5],
     [4,1,2,5,2],
     [1,6,3,2,1]]
print(chessboard_rec(A))
print(chessboard_iter(A))