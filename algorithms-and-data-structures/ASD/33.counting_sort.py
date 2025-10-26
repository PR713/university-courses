
def counting_sort(A,k):
    n = len(A)
    B = [None] * n
    C = [0]*k
    for x in A: C[x] += 1
    for i in range(1,k): C[i] += C[i-1]
    for i in range(n-1,-1,-1):
        #pętla od n-1,-1,-1 bo w C[i] mamy indeks na którym kończy się
        #występowanie danej wartości, więc aby było stabilne
        #musimy odtwarzać tablicę od tyłu
        B[C[A[i]]-1] = A[i] #A[i]-1 bo C[i] zawiera liczbę wartości
        #<= i, a indeksujemy od 0
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[i]


T = [1,2,0,2,3,0,4,0]
counting_sort(T,5)
print(T)
#złożoność O(n + k), dla k > n np k = n^2
#robi się to nieefektywne