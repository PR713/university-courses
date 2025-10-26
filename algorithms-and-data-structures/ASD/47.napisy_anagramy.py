#O(N) do tablic zliczamy w danym wyrazie ile razy występuje dana
#litera i potem te tablice sortujemy radix sortem
#O(NlogN) to sortowanie liter każdego wyrazu alfabetycznie
#i potem całe wyrazy w tablicy sortujemy i maks podciąg :)

#O(N), n <= N
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
        C[x[index]] += 1#na i-tym indeksie liczba wystąpień
    #danej litery w wyrazach w T, tzn z listy lists zliczamy
    #ile jest danych cyfr w kolejnych kolumnach x[index]
    #dzięki temu sortujemy napierw po ilości ostatniej litery
    #alfabetu w wyrazie (index = 25, potem przedostatniej 24...0)
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

T = ["tygrys","kot","wilk","trysyg","wlik","sygryt","likw","tygrys"]
print(max_podciąg_z_lists(radix_sort(T)))

