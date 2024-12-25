
def heapify(A,n,i):
    l = 2*i + 1 #left(i)
    r = 2*i + 2 #right(i)
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A,n,max_ind)
#Jeśli któreś dziecko ma większą wartość niż rodzic, to zamieniamy
#te wartości, żeby wartość największa znajdywała się na szczycie kopca.
#Następnie, dla dziecka, które zostało zamienione z rodzicem,
#rekurencyjnie wywołujemy funkcję heapify, aby upewnić się,
#że struktura kopca jest zachowana również dla tego poddrzewa.
#i wraz z rekurencją od dołu do góry naprawia się struktura kopca
def buildheap(A): #buduje kopiec zgodny z zasadami budowy kopca
    #dokładając swapując kolejne elementy
    n = len(A)
    for i in range(n//2 - 1,-1,-1):
        heapify(A,n,i)

def heapsort(A):
    n = len(A)
    buildheap(A)
    for i in range(n-1,0,-1): #zamienia kopiec w posortowaną listę
    #tzn odheapowuje drzewo, dodając za każdym razem największy element
    #będący na A[0] na koniec listy, a element z A[i] początkowo
    #z końca na początek i naprawia struktuę heap już dla listy
    #n-1 elementowej i znowu szuka największego będący wierzchołkiem
    #kopca na A[0]
        A[i], A[0] = A[0], A[i]
        heapify(A,i,0)
    return A

T = [1,5,4,2,7,4,3,2,8,1,3,6,9]
print(heapsort(T))
