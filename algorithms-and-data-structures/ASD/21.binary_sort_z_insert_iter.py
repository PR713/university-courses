
def binary_insertion_sort(T):
    n = len(T)
    for i in range(1, n):
        key = T[i] #binarne wstawianie kolejnych elementów
        left = 0
        right = i - 1
        while left <= right: #wyszukiwanie binarne
            mid = (left + right) // 2
            if T[mid] < key: #szukamy tymczasowego miejsca dla key
                left = mid + 1
            else:
                right = mid - 1
        T[left+1:i+1] = T[left:i] #przesuwamy o jedno w prawo, wycinając key
        T[left] = key #robimy miejsce dla key

#Szukamy właściwej pozycji dla aktualnego key względem aktualnie
#posortowanej części tablicy. Czyli wraz z zakresem tablicy w pętli
#(for i in range(1,n)) szukamy tam właściwego miejsca dla key.
#W następnych iteracjach 'i' znowu szukamy miejsca dla następnego key
#i wstawiamy go gdzieś w odpowiednie miejsce już trochę posortowanej
#lewej części tablicy // takie wstawianie binarne

T = [5, 2, 4, 6, 1, 3]
binary_insertion_sort(T)
print(T)