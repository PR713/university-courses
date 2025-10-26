
def pierwsza(x):
    if x < 2: return False
    if x == 2 or x == 3: return True
    if x % 2 == 0 or x % 3 == 0: return False
    i = 5
    while i * i <= x:
        if x % i ==0: return False
        i += 2
        if x % i ==0: return False
        i += 4
    return True

def komplementarne(tab):
    n = len(tab)
    odp = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if i != k or j != l:
                        suma = tab[i][j] + tab[k][l]
                        if pierwsza(suma):
                           odp[i][j] = True
                           odp[k][l] = True

    for i in range(n):
        for j in range(n):
            if odp[i][j] == False:
                tab[i][j] = 0
    for i in range(n):
        print(tab[i])

tab = [
    [2, 2, 2, 4],
    [2, 6, 3, 8],
    [9, 1, 2, 2],
    [2, 4, 17, 6]]
tab = [
    [2, 3, 2, 2],
    [2, 2, 2, 2],
    [2, 2, 2, 2],
    [2, 2, 6, 2]]
print(komplementarne(tab))
