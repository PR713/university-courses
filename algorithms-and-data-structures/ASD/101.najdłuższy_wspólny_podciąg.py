#A[0],...A[n-1]
#B[0],...B[m-1]
#chcemy znaleźć ich najdłuższy wspólny podciąg

#f(i,j) - długość najdłuższego wspólnego podciągu
#ciągów A[0],...,A[i] oraz B[0],...,B[j]
#rekurencja
#f(i,j) =
#albo ich ostatnie elementy są równe, albo nie
#jeśli A[i] = B[j] to f(i,j) = f(i-1,j-1) + 1
#jeśli A[i] != B[j] to f(i,j) = max(f(i-1,j) , f(i,j-1))
#albo dopasujemy z jednej cofając się o jeden, albo z drugiej
#f(-1,x) = f(x,-1) = 0
#żeby móc odczytać musimy wiedzieć które z 3 przypadków wzięliśmy

def longest_common_subsequence(A,B):
    a = len(A)
    b = len(B)
    F = [[ None for _ in range(b+1)] for _ in range(a+1)]
    #L[i][j] contains length of LCS of X[0..i-1]
    #and Y[0..j-1]
    for i in range(a+1):
        for j in range(b+1):
            if i == 0 or j == 0:#f(x,0) = f(0,x) = 0
                F[i][j] = 0
            elif A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[a][b]
#--------------------------------------------
#lub
def longest_common_subsequence2(A,B):
    a = len(A)
    b = len(B)
    F = [[ None for _ in range(b+1)] for _ in range(a+1)]
    F[-1][-1] = 0
    #tu F[i][j] to LCS A[0],...A[i] i B[0],...B[j]
    #po prostu w ostatniej kolumnie i wierszu mamy '-1'
    #a wyżej mamy w pierwszej kolumnie i pierwszym wierszu
    for i in range(a+1): F[i][-1] = 0
    for j in range(b+1): F[-1][j] = 0
    for i in range(a):
        for j in range(b):
            if A[i] == B[j]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[a-1][b-1]

X = "AGAGTAB"
Y = "GXATXAYB" #AGTAB
print(longest_common_subsequence(X,Y))
print(longest_common_subsequence2(X,Y))
