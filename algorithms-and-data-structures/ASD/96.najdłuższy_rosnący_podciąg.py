#niekoniecznie spójny

def lis(A):
    n = len(A)
    F = [1]*n
    p = [-1]*n #parent
    for k in range(1,n):
        for t in range(k):
            if A[t]<A[k] and F[k] < F[t] + 1:
                F[k] = F[t] + 1
                p[k] = t
    return max(F),F,p

def print_sol(A,p,k):
    if p[k] != -1:
        print_sol(A,p,p[k])
    print(A[k])
