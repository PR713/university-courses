#Radosław Szepielak
#Tworzę nową listę A, która przechowuje pierwszych p elementów
#z tablicy T od '0 do p-1' indeksu włącznie. Następnie utworzoną listę A
#sortuję algorytmem heapsort, budując kopiec zgodny z założeniami heap sort.
#Gdy już mam posortowaną listę A, kolejnym krokiem jest znalezienie k-tego
#największego elementu tzn. elementu pod indeksem 'a-k', gdzie a = len(A).
#Dodaję tę wartość A[a-k] do 'sum'. Następnie szukaniem binarnym znajduję
#indeks, pod którym w posortowanej liście A znajduje się element pierwszy
#z tablicy T i go usuwam z listy A. Potem szukam binarnie indeksu,
#w którym należy wstawić następny element z tablicy T i go wstawiam do listy A
#przesuwając elementy na większych indeksach w prawo. W ten sposób w pętli for
#przesuwam cały czas wycinek p - elementowy tablicy T o kolejne indeksy w prawo,
#który wraz z usuwaniem i dodawaniem kolejnych elementów z T, jest cały czas
#posortowany. Jednocześnie zwiększam sumę o kolejne wartości A[a-k].
#
#Złożoność czasowa algorytmu to O(np).
#Złożoność pamięciowa algorytmu to O(n+p)

from zad2testy import runtests

def ksum(T, k, p):

    def heapify(A, a, i):
        l = 2 * i + 1  # left(i)
        r = 2 * i + 2  # right(i)
        max_ind = i
        if l < a and A[l] > A[max_ind]:
            max_ind = l
        if r < a and A[r] > A[max_ind]:
            max_ind = r
        if max_ind != i:
            A[i], A[max_ind] = A[max_ind], A[i]
            heapify(A, a, max_ind)

    def buildheap(A):  # buduje kopiec zgodny z zasadami budowy kopca
        a = len(A)
        for i in range(a // 2 - 1, -1, -1):
            heapify(A, a, i)

    def heapsort(A):
        a = len(A)
        buildheap(A)
        for i in range(a - 1, 0, -1):  # zamienia kopiec w posortowaną listę
            A[i], A[0] = A[0], A[i]
            heapify(A, i, 0)
        return A

    def binary_search(A, target):
        left = 0
        right = len(A) - 1

        while left <= right:
            mid = (left + right) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    n = len(T)
    tmp = T[0]
    A = T[0:p]
    A = heapsort(A)
    a = len(A)
    sum = A[a - k]
    for el in range(p, n):
        del A[binary_search(A, tmp)]  # usuwanie pierwszego elementu z wycinku z T
        A.insert(binary_search(A, T[el]), T[el])
        sum += A[a - k]
        tmp = T[el - p + 1]  # zapamiętuję element do usunięcia w następnej iteracji
    return sum  # suma z0 + z1 + z2 + . . . + z_(n−p)
    return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
