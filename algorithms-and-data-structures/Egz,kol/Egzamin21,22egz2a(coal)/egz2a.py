from egz2atesty import runtests

def coal( A, T ):
    n = len(A)
    cart = [T]*n
    j = 0
    for i in range(n): #i-ty transport
        for j in range(n):
            if cart[j] - A[i] >= 0:
                cart[j] -= A[i]
                if i == n-1:
                    return j
                break


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
