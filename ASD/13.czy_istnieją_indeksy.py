
#Dana jest posortowana tablica A[1...n] oraz liczba x.
#Proszę napisać program, który stwierdza czy istnieją indeksy
# i  oraz j takie, że A[i] + A[j] = x

# 0, 1, 3, 10, 12
# x = 11
#przesunięcie j zwiększa, i zmniejsza
A = [0,1,3,10,12]
def indeksy(A,x):
    j = len(A) - 1
    i = 0
    while i != j:
        if A[i] + A[j] > x:
            j -= 1
        elif A[i] + A[j] < x:
            i += 1
        else:
            return (i,j)

print(indeksy(A,11))