def digits(n):
    if n == 0:
        return 1
    res = 0
    while n != 0:
        n //= 10
        res += 1
    return res


def countingsort(A, divisor):
    counter_length = 10 # 10 cyfr
    n = len(A) #n liczb
    counter = [0]*counter_length
    for num in A:
        counter[(num//divisor)%10] += 1
        #bierzemy kolejno ostatnią cyfrę, przedostatnią...

    for i in range(1,counter_length):
        counter[i] += counter[i-1]

    output = [0] * n
    for i in range(n-1,-1,-1):
        output[counter[(A[i]//divisor)%10] - 1] = A[i]
        counter[(A[i]//divisor)%10] -= 1

    return output

def radixsort(A):
    k = digits(max(A))
    for i in range(k):
        A = countingsort(A, 10**i)
    return A
#O(nk), n liczba liczb, k długość najdłuższej liczby
from random import randrange
A = [randrange(1,101) for _ in range(15)]
print(A)
print(radixsort(A))