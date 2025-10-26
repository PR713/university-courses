def ciag_geo(tab):
    n = len(tab)
    cnt = 3  #minimalna dlugosc
    iloraz_curr = 0
    k, l = 1, 1
    for i in range(n - 1):  # wiersze
        for j in range(n - 1):  # kolumny, tab[l][k]
            dlugosc = 2
            l = i + 1 #lub jakaś zmienna k, potem k+=1 i tab[i+k+1][j+k+1]/tab[i+k][j+k]
            k = j + 1
            iloraz_curr =  tab[l][k]/tab[i][j]
            while l != n-1 and k != n-1:#żeby skosem nie wyjść poza tab
                iloraz_nast = tab[l+1][k+1]/tab[l][k]
                if iloraz_curr == iloraz_nast:
                    dlugosc += 1
                    l += 1
                    k += 1
                    if dlugosc >= cnt:  # jeśli znajdziemy dłuższy
                         cnt = dlugosc
                else: #czyli iloraz różny
                    break#w kolejnych wierszach i tak sprawdzimy dalszy skos
    if cnt >= 3: return True, 'Dlugość ciągu geom. to', cnt
    return False

tab = [[1,2,3,4,5],
       [3,4,4,7,9],
       [5,10,6,8,6],
       [7,15,11,12,10],
       [1,2,3,4,5]]
print(ciag_geo(tab))