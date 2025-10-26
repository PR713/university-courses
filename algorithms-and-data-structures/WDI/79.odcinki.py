def inter(A, B):
    return (A[0] >= B[0] and A[0] <= B[1]) or (A[1] >= B[0] and A[1] <= B[1])

def odcinki(T):
    n = len(T)
    U = [False]*n

    def rek(i,suma):
        if i == n:
            return suma == 2022

        valid_candidate = True
        for x in range(0, i):
            if U[x] and inter(T[i], T[x]):
                #czyli jeśli wzięty wcześniej i teraz następny się
                #nie pokrywają to ustawia go niżej na True
                valid_candidate = False
                break

        if valid_candidate:
            U[i] = True
            if rek(i + 1, suma + T[i][1] - T[i][0]):
                return True
            U[i] = False
        return rek(i + 1, suma)

    return rek(0, 0)