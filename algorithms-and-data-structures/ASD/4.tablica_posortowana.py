
# T - posortowana niemalejąco tablica liczb
# x - jakaś liczba
# znaleźć i,j - indeksy, T[j] - T[i] = x

def func(T,x):
    n = len(T)
    i = 0
    j = 0
    while T[j] - T[i] != x:
        while T[j] - T[i] > x:
            if i == n-1:
                return False
            i += 1
        while T[j] - T[i] < x:
            if j == n-1:
                return False
            j += 1
    return i,j

T = [0,1,2,3,3,5,7,8,9]
print(func(T,3))
