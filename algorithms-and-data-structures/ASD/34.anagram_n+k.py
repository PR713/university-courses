
#Dwa słowa A i B nad alfabetem k - elementowym
#sprawdzić czy A i B są anagramami

def anagram(A,B,k): #O(n+k)
    if len(A) != len(B):
        return False
    n = len(A)
    T = [0 for _ in range(k)]
    for i in range(n):
        T[A[i]] += 1
        T[B[i]] -= 1
    for i in range(k):
        if T[i] != 0:
            return False
    return True

print(anagram([1,2,3],[3,2,2],4)) #False, dla [3,2,1] True