
def partition(arr,low,high):
    pivot = arr[high] #pivot ostatni element
    i = low - 1

    for j in range(low,high):
        if arr[j] <= pivot:#skoro mniejszy to
            #wywala do lewej, a ten ciut większy
            #tzn T[i] w prawo przesuwa
            i += 1 #i tam gdzie j lub wcześniej
            arr[i], arr[j] = arr[j], arr[i]
    #zamieniamy następny po i tzn i + 1 bo będzie on na pewno
    # >= od obecnego pivota :)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    #na tą chwilę pivot będący teraz na indeksie i+1
    #ma po lewej <= od niego a na prawo > od niego
    #dlatego potem rekurencyjnie dla tych po lewej od niego i dla
    #tych na prawo niezależnie bo on już jest na dobrym miejscu :)
    return i + 1 #wyznacza pozycję kolejnego pivota

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr,low,high)
        quicksort(arr,low,pivot_index - 1)
        quicksort(arr,pivot_index + 1, high)
""" lub bez rekurencji ogonowej
def quicksort(arr, low, high):
    while low < high:
        pivot_index = hoare(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        low = pivot_index + 1"""
arr = [7,2,1,6,8,5,3,4,0]
quicksort(arr,0, len(arr) - 1)
print(arr)

def quickselect(arr,low,high,k):#<= bo jak zostanie 1 el. też sprawdzamy go
    if low <= high: #element na k-tym indeksie po posortowaniu
        pivot_index = partition(arr,low,high)
        if pivot_index == k:
            return arr[pivot_index] #rzadko od razu trafimy
        elif pivot_index < k:
            return quickselect(arr, pivot_index+1, high,k)
        else:
            return quickselect(arr, low, pivot_index-1,k)

arr = [7,2,1,6,8,5,3,4,0]
print(quickselect(arr,0,len(arr)-1, 4))
