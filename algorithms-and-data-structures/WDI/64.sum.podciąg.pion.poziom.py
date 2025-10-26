def series(tab):
    n = len(tab)
    max_sum = suma = 0
    for y in range(n):#przesuwanie się - czy istnieje o większej sumie ale krótszy
        for x in range(n): #to samo ^ ale w kolumnach
            for i in range(1, 11):#długośc podciągu
                if i + y < n: #sumowanie po wierszach ↓
                    suma = 0
                    for j in range(y, i + y + 1):#+1-> podciąg będzie min 2 elem.
                        suma += tab[j][x] #ale jak przejdziemy całą kolumnę to przechodzimy potem po skosie o 1 (bo wiersz dalej) i znowu
                    max_sum = max(max_sum, suma)
                if i + x < n: #sumowanie po kolumnach →
                    suma = 0
                    for j in range(x, i + x + 1):
                        suma += tab[y][j]
                    max_sum = max(max_sum, suma)
    return max_sum

tab = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
print(series(tab))