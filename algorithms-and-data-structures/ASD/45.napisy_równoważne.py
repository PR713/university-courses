
def is_palindrome(str):
    if str == str[::-1]: return True
    return False

def partition(T,low,high):
    i = low - 1
    pivot = T[high]
    for j in range(low,high):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[high] = T[high], T[i+1]
    return i + 1

def quicksort(T,low,high):
    if low < high:
        pivot_index = partition(T,low,high)
        quicksort(T,low,pivot_index-1)
        quicksort(T,pivot_index + 1, high)
    return T

def g(T):
    for i in range(len(T)):
        if not is_palindrome(T[i]):
            T.append(T[i][::-1])

    quicksort(T,0,len(T)-1)
    res = 1
    curr = 1
    for i in range(len(T)-1):
        if T[i] == T[i+1]:
            curr += 1
            res = max(res,curr)
        else:
            curr = 1
    return res

T = ["pies","mysz","kot","kogut","tok","seip","kot"]
print(g(T))