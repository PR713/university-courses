#Wydawanie monet, Mamy daną tablicę
#M z nominałami monet oraz liczbę B.
#ile monet minimalnie trzeba użyć żeby wydać B.

#F(sum) - minimalna liczba monet żeby otrzymać sumę
#F(sum) = min(F(sum-M[i]) + 1)  dla i = 0,...,n-1
#F(M[i]) = 1 lub F(0) = 0
#przez spamiętywanie czyli rekurencyjnie
def minMonety(M,B):
    F = [None for _ in range(B+1)]
    #P= [None for _ in range(B+1)]
    #P[B] nominał monety jaką trzeba użyć żeby
    #otrzymać sumę B
    F[0] = 0
    return minMonetyrek(F,M,B)

def minMonetyrek(F,M,B):
    if F[B] != None:
        return F[B]

    result = float('inf')
    for m in M:
        if B - m >= 0:#and result > minMonetyrek(F,M,b-m):
            #P[B] = m, result = minMonetyrek(F,M,b-m)
            result = min(result,minMonetyrek(F,M,B-m))
    result += 1
    F[B] = result
    return result

def print_sol(P,B):
    while B > 0:
        print(P[B])
        B -= P[B] #potem już sumę mniejszą P[B'-P[B]]


######################
#iteracyjnie

def money(T, M): # T - kwota, M - nominaly
    n = T + 1
    F = [ float('inf') for _ in range(n) ]
    F[0] = 0

    for x in range(1, n):#dla każdej kwoty
        for m in M: #sprawdzamy wszystkie nominały
            if x - m >= 0:
                F[x] = min( F[x], F[ x - m ] + 1 )

    return F[T]