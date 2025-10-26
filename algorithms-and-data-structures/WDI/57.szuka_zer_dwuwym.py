
def szuka_zera(tab):
    n = len(tab)
    wiersz = [False] * n
    kolumna = [False] * n
    for i in range(n):
        for j in range(n):
            if tab[i][j] == 0:
                wiersz[i] = True
                kolumna[j] = True

    if not (wiersz[i] and kolumna[j]):
            return False
    return True


tab = [[0,2,3,4],
       [34,5,0,7],
       [56,0,4,3],
       [3,7,6,0]]
print(szuka_zera(tab))