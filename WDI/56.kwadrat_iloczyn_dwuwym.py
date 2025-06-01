def kwadrat(tab,iloczyn):
    n = len(tab)
    for i in range(3, n+1, 2):#dlugosc boku, szukamy od lewego dolnego rogu
        for j in range(n-i+1): #wartość x lewego górnego wierzch.
            for k in range(n-i+1): #wartość y lewego górnego wierzch.
                jeden = tab[k][j] #lewy górny
                dwa = tab[k][j + i - 1] #prawy górny
                trzy = tab[k + i - 1][j] #lewy dolny
                cztery = tab[k + i - 1][j + i - 1]
                if jeden*dwa*trzy*cztery == iloczyn:
                    return True, "wiersz", k+i//2, "kolumna", j+i//2

tab = [[2,2,1,2,2],
       [2,1,1,1,1],
       [1,1,1,4,1],
       [1,1,1,1,1],
       [2,1,1,1,24]]
for i in range(len(tab)):
    print(tab[i])
print(kwadrat(tab,16))