from kol1btesty import runtests

def count(T):
    n = len(T)
    lists = [[0]*26 for _ in range(n)] #dla każdego wyrazu tworzymy listę
    for i in range(n):
        for j in range(len(str(T[i]))):
            lists[i][ord(T[i][j]) - 97] += 1
    return lists

def counting_sort(A,index,N):
    n = len(A)
    B = [[0]*26 for _ in range(n)]
    C = [0]*(N+1)

    for x in A: #x to tablica reprezentująca wyraz
        C[x[index]] += 1
    for i in range(1,N+1):
        C[i] += C[i-1]

    for i in range(n-1,-1,-1):
        B[C[A[i][index]] - 1] = A[i]
        C[A[i][index]] -= 1
    return B

def radix_sort(T):
    lists = count(T) #wyrazy zapisane jako liczba wystąpień danej literki
    N = 0 #łączna długość wyrazów w T
    for i in range(len(T)):
        N += len(str(T[i]))
    n = len(T)

    for i in range(25,-1,-1):
        res = counting_sort(lists,i,N) #przypisujemy coraz
        # bardziej posortowaną listę
        lists = res

    return res

def max_podciąg_z_lists(tab):
    cnt = 1
    cnt_max = 0
    for i in range(len(tab)-1):
        if tab[i] == tab[i+1]:
            cnt += 1
        else:
            cnt = 1
        if cnt > cnt_max:
            cnt_max = cnt
    return cnt_max

def f(T):
    return max_podciąg_z_lists(radix_sort(T))


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
