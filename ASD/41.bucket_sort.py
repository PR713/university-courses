
def selsort(A):
    for i in range(len(A)):
        min_val = i
        for j in range(i+1,len(A)):
            if A[min_val] > A[j]:
                min_val = j
        A[i], A[min_val] = A[min_val], A[i]

def bucket_sort(T,sorting_function):
    n = T[0]
    l = len(T)
    for i in range(l):
        if T[i] > n:
            n = T[i] #szukanie max

    buckets = [[] for _ in range(l+1)]

    for x in T:
        i = ((x/n) * l)
        buckets[int(i)].append(x)

    result = []
    #[] -> false
    for bucket in buckets:
        if bucket:
            sorting_function(bucket) #selsort(bucket)
        for x in bucket:
            result.append(x)
    return result

import random
A = [random.random() for _ in range(5)]
print(bucket_sort(A,selsort))
A = [0.1,0.23,0.0121,0.5,0.67,0.43,0.9,0.75]
print(bucket_sort(A,selsort))
