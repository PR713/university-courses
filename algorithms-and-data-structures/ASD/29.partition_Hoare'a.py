def hoare(A, p, r):
    ind_left = p
    ind_right = r - 1 #bo na A[r] jest pivot i potem ustawimy
    #go poprawnie a w drugim podejściu p-1 i r+1, i to co zwracamy
    #jest punktem podziału ale A[j] nie musi być na razie poprawny
    #dlatego tutaj porównujemy cały czas z A[r] bo go nie ruszamy
    #a na dole tylko wartość zapamiętujemy :)
    while ind_left <= ind_right:
        if A[ind_left] > A[r] and A[ind_right] < A[r]:
            A[ind_right], A[ind_left] = A[ind_left], A[ind_right]
            ind_left += 1
            ind_right -= 1
        elif A[ind_left] > A[r]:
            ind_right -= 1
        elif A[ind_right] < A[r]:
            ind_left += 1
        else:
            # oba dobre
            ind_right -= 1
            ind_left += 1
    A[ind_left], A[r] = A[r], A[ind_left]
    #teraz na lewo od pivota są < na prawo >=
    #bo zamieniamy pivota i na pewno on już jest dobrze
    return ind_left



def quicksort(arr, low, high):
    while low < high:
        pivot_index = hoare(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        low = pivot_index + 1


T = [15, 6, 7, 33, 2, 3, 4, 7, 2, 3]
quicksort(T, 0, len(T) - 1)
print(T)


#lub
#Ten drugi Hoare nawet z rekurencją z ifem musi mieć
#jedno wywołanie od left do pivot, drugie od pivot+1 do right
#a normalnie left, pivot - 1, drugie pivot+1, right
#coś ma inaczej indeksy więc inaczej rekurencja ogonowa
#jakby zawsze się o -1 różni i trzeba bez ogonowej dwa przypadki
#bo tutaj indeks j nie oznacza gdzie jest już na pewno dobrze
#ustawiony pivot w przeciwieństwie do tego wyżej, tylko określa
#że po lewej od j są elementy <= pivotowi a na prawo > pivot
#więc pivot nie musi być dokładnie na j tylko wewnątrz tablicy
def _quick_sort(arr, left_idx, right_idx):
    while left_idx < right_idx:
        pivot_position = partition_hoare(arr, left_idx, right_idx)

        if pivot_position - left_idx < right_idx - pivot_position:
            _quick_sort(arr, left_idx, pivot_position)
            left_idx = pivot_position + 1  # I removed a tailing recursion
        else:
            _quick_sort(arr, pivot_position + 1, right_idx)
            right_idx = pivot_position  # I removed a tailing recursion

def partition_hoare(A, p, r):
    x = A[p]
    i = p - 1
    j = r + 1
    while True:
        i += 1
        while A[i] < x:
            i += 1
        j -= 1
        while A[j] > x:
            j -= 1

        if i >= j:
            return j
        #tu pod indeksem j nie musi być na pewno pivot
        #i to być jego właściwa pozycja tylko to jest punkt
        #podziału tablicy na >= od pivota i < od wartości pivota
        A[i], A[j] = A[j], A[i]


T = [15, 6, 7, 33, 2, 3, 4, 7, 2, 3]
_quick_sort(T, 0, len(T) - 1)
print(T)

