
#zaimplementować quicksort, żeby zużywał O(log(n)) pamięci na stosie

def partition(arr,low,high):
    pivot = arr[high] #pivot ostatni element
    i = low - 1

    for j in range(low,high):
        if arr[j] <= pivot:#skoro mniejszy to
            #wywala do lewej, a ten ciut większy
            #tzn T[i] w prawo przesuwa
            i += 1 #i tam gdzie j lub wcześniej
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1 #wyznacza pozycję kolejnego pivota

def quicksort(arr, low, high):
    while low < high:
        pivot_index = partition(arr,low,high)
        quicksort(arr,low,pivot_index - 1)
        low = pivot_index + 1

arr = [7,2,1,6,8,5,3,4,0]
quicksort(arr,0, len(arr) - 1)
print(arr)

#def quicksort_(tab, p, k):
#    while p < k:
#        i = partition(tab, p, k)
#        if i - 1 - p > k - i: #sortujemy mniejszy kawałek
#            quicksort(tab, i+1, k)
#            k = i - 1
#        else:
#            quicksort(tab, p, i-1)
#            p = i+1
#    return tab