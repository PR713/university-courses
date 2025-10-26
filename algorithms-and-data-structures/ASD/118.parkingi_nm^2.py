# f(i, j) = minimalna suma odległości biurowców
# z pozycji X[0], . . . , X[i] do przydzielonych im działek,
# przy założeniu że biurowiec z pozycji X[i] ma przydzieloną działkę
# z pozycji Y[j].
# f(i,j) = abs(X[i]-Y[j]) + min( f(i-1,j-1),... f(i-1,i-1))


def parking(X, Y):
    n, m = len(X), len(Y)
    F = [[float('inf') for _ in range(m)] for _ in range(n)]

    for j in range(m):
        F[0][j] = abs(X[0]-Y[j])

    for i in range(1,n):
        for j in range(m):
            for k in range(i-1,j):
                F[i][j] = min(F[i][j], abs(X[i]-Y[j]) + F[i-1][k])
    result = float('inf')
    for j in range(n-1,m):
        result = min(result, F[n-1][j])
    return result
