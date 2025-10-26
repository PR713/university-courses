def sito(n):
    a = [True] * (n+1) # przedział od <0, n> ale n+1 el. w tablicy
    a[0] = False
    a[1] = False
    i = 2
    while i*i < n:
        if a[i]:
            for j in range(i*i, n+1, i):
                a[j] = False
        i+=1
    return a

n = 1000
a = sito(n)

for liczba in range(2, 1000, 2):
    for i in range(n+1):
        for k in range(n+1):
           if a[i] == True and a[k] == True and liczba == i + k and i <= k:
                print(f'Szukany rozkład dla {liczba} to: {i},{k}')
                break