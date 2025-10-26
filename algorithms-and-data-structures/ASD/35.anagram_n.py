import numpy
#Dwa słowa A i B nad alfabetem k - elementowym
#sprawdzić czy A i B są anagramami

def anagram(A,B,k): #O(n)
    if len(A) != len(B):
        return False
    n = len(A)
    T = numpy.empty(k)

    for i in range(n):
        T[A[i]] = 0
        T[B[i]] = 0

    for i in range(n):
        T[A[i]] += 1
        T[B[i]] -= 1

    for i in range(n):
        if T[A[i]] != 0 and T[B[i]] != 0:
            return False

    return True

print(anagram([1,2,3],[3,2,2],4)) #False, dla [3,2,1] True