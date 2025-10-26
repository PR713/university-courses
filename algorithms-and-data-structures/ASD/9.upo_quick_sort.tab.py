def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_pivot = [x for x in arr[1:] if x <= pivot]
        greater_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_pivot) + [pivot] + quick_sort(greater_pivot)

# Przykład użycia:
my_list = [1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = quick_sort(my_list)
print(sorted_list)