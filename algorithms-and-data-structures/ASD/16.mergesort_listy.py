
def MergeSort(A,Left,Right): #dzieli na pół
    def merge(A,Left,Mid,Right):#łączy
        Len1 = Mid - Left + 1
        Len2 = Right - Mid
        Left_A = A[Left:Mid+1] # Left - Mid
        #Left_A = [A[i] for i in range(Left,Mid+1)]
        Right_A = A[Mid+1:Right+1] #Mid+1 - Right
        Left_index = Right_index = 0
        Main_index = Left

        while Left_index < Len1 and Right_index < Len2:
            if Left_A[Left_index] <= Right_A[Right_index]:
                A[Main_index] = Left_A[Left_index]
                Left_index += 1
            else:
                A[Main_index] = Right_A[Right_index]
                Right_index += 1
            Main_index += 1
        while Left_index < Len1:
            A[Main_index] = Left_A[Left_index]
            Left_index += 1
            Main_index += 1

        while Right_index < Len2:
            A[Main_index] = Right_A[Right_index]
            Right_index += 1
            Main_index += 1

    if Left < Right:
        Mid = (Right+Left)//2
        MergeSort(A,Left,Mid) #lewa
        MergeSort(A,Mid+1,Right) #prawa
        merge(A,Left,Mid,Right)

from random import randint
A = [randint(1,20) for _ in range(20)]
print(A)
MergeSort(A,0,len(A)-1)
print(A)


#lub
def MergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        # Tworzymy lewą i prawą połowę
        L = A[:mid]
        R = A[mid:]
        # Rekurencyjnie sortujemy obie połowy
        MergeSort(L)
        MergeSort(R)
        i = j = k = 0 #k czyli main_ind zerujemy w każdej mniejszej
        #części tablicy A jaką dostajemy żeby wypełnić ją od lewej do prawej
        #bo przekazujemy jako nowe listy, a nie oryginalną i indeksy podziału
        # Scalanie posortowanych list
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        # Kopiowanie pozostałych elementów L[], jeśli są
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        # Kopiowanie pozostałych elementów R[], jeśli są
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1