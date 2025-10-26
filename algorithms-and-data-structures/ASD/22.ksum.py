
def ksum(T,k,p):
    n = len(T)
    def binary_insertion_sort(A):
        a = len(A)
        for i in range(1, a):
            key = A[i]
            left = 0
            right = i - 1
            while left <= right:  # wyszukiwanie binarne
                mid = (left + right) // 2
                if A[mid] < key:  # szukamy tymczasowego miejsca dla key
                    left = mid + 1
                else:
                    right = mid - 1
            A[left + 1:i + 1] = A[left:i]  # przesuwamy o jedno w prawo
            A[left] = key
        return A

    def binary_search(A, target): #dla już posortowanej listy P
        left = 0
        right = len(A) - 1

        while left <= right:
            mid = (left + right) // 2
            if A[mid] == target:
                return mid #na pewno znajdziemy
            elif A[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


    tmp = T[0]
    A = T[0:p]
    A = binary_insertion_sort(A)
    a = len(A)
    sum = A[a-k]
    for el in range(p,n):#tutaj binary search dla T[del] i potem T[el]
        del_index = binary_search(A,tmp)
        del A[del_index]
        A.insert(binary_search(A,T[el]), T[el])
        sum += A[a-k]
        tmp = T[el-p+1] #kolejne elementy z T
    return sum

T = [7,9,1,5,8,6,2,12]
print(ksum(T,4,5))
#p*log(p) + n * ( 2log(p) + p) = O(np)







