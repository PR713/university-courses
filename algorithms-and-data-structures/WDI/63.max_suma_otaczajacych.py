
def suma(tab):
    n = len(tab)
    max_suma = 0
    for i in range(1,n-1):#bez obrzeży, z nimi to oddzielne przypadki wiele ifów
        for j in range(1,n-1):
            suma = -tab[i][j]
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    suma += tab[k][l]
                    if suma > max_suma:
                        max_suma = suma
                        x = i
                        y = j
    return max_suma, 'wiersz: ', x, 'kolumna:', y

tab = [[10,2,3,4],
       [1,1,1,1],
       [2,2,2,2],
       [5,10,6,7]]
print(suma(tab))