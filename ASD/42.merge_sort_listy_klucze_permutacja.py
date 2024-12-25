def merge_sort_with_keys(A, P):
    if len(A) <= 1:
        return A #lub samo return, warunek końca rekurencji
    #w miarę powrotu rekurencji zaczyna z powrotem scalać

    mid = len(A) // 2
    left_A = A[:mid]
    right_A = A[mid:]
    left_P = P[:mid]
    right_P = P[mid:]

    merge_sort_with_keys(left_A, left_P)
    merge_sort_with_keys(right_A, right_P)
    #przekazujemy wycinki ^ do rekurencji, tzn A = left_A lub right_A
    #więc nie trzeba pamiętać main_indeks itp jak w zad 16
    #tzn  merge_sort(left_half) i merge_sort(right_half)
    #zamiast MergeSort(A,Left,Mid) i MergeSort(A,Mid+1,Right)
    i = j = k = 0 #left_ind, right_ind, main_ind ale dla wycinka A

    while i < len(left_A) and j < len(right_A):
        if left_P[i] <= right_P[j]:
            A[k] = left_A[i]
            P[k] = left_P[i]
            i += 1
        else:
            A[k] = right_A[j]
            P[k] = right_P[j]
            j += 1
        k += 1

    while i < len(left_A):
        A[k] = left_A[i]
        P[k] = left_P[i]
        i += 1
        k += 1

    while j < len(right_A):
        A[k] = right_A[j]
        P[k] = right_P[j]
        j += 1
        k += 1


A = [3, 1, 4, 2, 6, 5, 8]
P = [3, 2, 1, 6, 4, 5, 0]
#8,4,1,3,6,5,2
merge_sort_with_keys(A, P)
print("Posortowana tablica A względem kluczy z tablicy P:", A)
