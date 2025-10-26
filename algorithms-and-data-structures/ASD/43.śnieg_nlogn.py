
def heapify(A,n,i):
    l = 2*i + 1
    r = 2*i + 2
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A,n,max_ind)

def snow(S):
    n = len(S)
    sum_snow, pom = 0, 0
    index = n - 1

    for i in range(n//2 - 1, -1, -1):
        heapify(S,n,i)

    while S[0] - pom > 0 and index >= 0:
        S[0], S[index] = S[index], S[0]
        sum_snow += S[index] - pom #czyli najwyższy element
        heapify(S,index,0)
        pom += 1
        index -= 1
    return sum_snow

A = [4,24,1,0,2,6]
B = [60,40,100,2,50]
print(snow(A))
print(snow(B))
#a kolejność nie ma znaczenia
#60 + (50-1) + (40-2) + (100-3) = 244
#100 + (60-1) + (50-2) + (40-3) = 244
#lub wbudowanym zamiast heapsorta to  S.sort i lecimy while
#S[index] - pom > 0 and index >= 0