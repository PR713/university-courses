#Posortować tablicę n - elementową liczb
#z zakresu 0,1,..., n^2-1
# x = A*N + B
#radix_sort od tyłu np n = 5
# dla 23 mamy 4 r 3 i sortujemy od reszt potem po całkowitej części
#zachowujemy dzięki temu stabilność sortowania
def counting_sort_z_resztami(A, k):
    n = len(A)
    B=[None]*n
    C = [0]*k
    for x in A: C[x%k] +=1
    for i in range(1,k): C[i] += C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i]%k] - 1] =A[i]
        C[A[i]%k] -=1
    for i in range(n):
        A[i] = B[i]
def counting_sort_calkowite(A, k):
    n = len(A)
    B=[None]*n
    C = [0]*k
    for x in A: C[x//k] +=1
    for i in range(1,k): C[i] += C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i]//k] - 1] =A[i] #pierwszy element
        #na przykład to ten z największą resztą %k więc
        #on ma być jako pierwszy, potem będą też z takim
        #samym //k ale mniejszą lub równą resztą %k
        C[A[i]//k] -=1
    for i in range(n):
        A[i] = B[i]

def sort_(A, n):
    counting_sort_z_resztami(A,n)
    counting_sort_calkowite(A,n)
    return A

print(sort_([24,10,4,6,7,3],5)) #zakres 0,..., 25-1