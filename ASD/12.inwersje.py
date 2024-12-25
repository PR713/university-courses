
#Mając na wejściu tablicę A zwraca liczbę inwersji i < j  A[j] < A[i]
#Chyba merge sort ale na normalnych tablicach z A//2
def mergesort(T,p,q): #p - początek, q - koniec
    def merge(T, p, m, q):
        len1 = m - p + 1
        len2 = q - m
        L = T[p:m + 1]
        R = T[m + 1:q + 1]
        left = right = 0
        main_ind = p
        cnt = 0
        while left < len1 and right < len2:
            if L[left] <= R[right]:
                T[main_ind] = L[left]
                left += 1
            else:
                cnt += len1 - left #od długości listy - ile wstawiono,
            #dzięki temu wiemy ile jest większych od tego który chcemy wstawić
                T[main_ind] = R[right]
                right += 1
            main_ind += 1

        while left < len1:
            T[main_ind] = L[left]
            left += 1
            main_ind += 1

        while right < len2:
            T[main_ind] = R[right]
            right += 1
            main_ind += 1

        return cnt

    inversion = 0
    if p < q:
        m = (p + q)//2
        inversion += mergesort(T,p,m)
        inversion += mergesort(T,m+1,q)
        inversion += merge(T,p,m,q)
    return inversion

#inwersje rekursywnie które były niżej do góry
#T = [1,4,3,5,2,6]
T = [3,4,1,2,7,5,6]
print(mergesort(T,0,len(T)-1))
#najpierw proces dzielenia tablicy na pojedyncze elementy odbywa się
#w dół drzewa rekursji (przekazujemy większe tablice), ale następnie
#rekurencyjne sortowanie i scalanie odbywają się w górę drzewa
#rekursji (czyli sortowanie pojedynczych potem par, czwórek w górę,
#bo wtedy zostawiliśmy indeksy w danym wywołaniu merge).