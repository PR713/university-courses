
#zaimplementować quick sort bez rekurencji

def partition(array, low, high):
    i = (low - 1)
    x = array[high]

    for j in range(low, high):
        if array[j] <= x:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1



def I_QuickSort(array, low, high):
    #  auxiliary stack
    size = high - low + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        # sorted array
        p = partition(array, low, high)

        # push left side to stack
        #dodawanie kolejnych granic podziału tablicy na stos
        #bez 'p' - pivota bo już jest na dobrym miejscu
        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        #  push right side to stack
        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high



tab = [7,11,15,6,7,33,2,3,4,7,9,12,8]
I_QuickSort(tab, 0, len(tab)-1)
print(tab)