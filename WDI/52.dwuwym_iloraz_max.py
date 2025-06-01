
def maks_iloraz(T):
    column = [0 for _ in range(4)]#załóżmy że tablica jest 5 x 5
    row = [0 for _ in range(4)] #przechowuje sumę el. w danym wierszu
    n = len(T) #ilość wierszy
    m = n #z zał. tablica jest N x N np 5 x 5
    for j in range(n):
        for i in range(m):
            row[j] += T[j][i] #sumuje wiersze
            column[i] += T[j][i]#sumuje kolumny

    iloraz_max = -50
    for j in range(n):
        for i in range(m):
            if row[j] == 0: break #bo dzielimy przez zero więc bierzemy j większe
            if column[i]/ row[j] > iloraz_max:
                iloraz_max = column[i]/row[j]
                x = i
                y = j
    print(column, row)
    return f'Największy iloraz to {iloraz_max} dla kolumny {x} i wiersza {y}'

T = [[1,2,3,4],[9,8,7,6],[3,80,2,6],[3,7,8,1]]
#T = [[-1,-2,-3,-4],[9,8,7,-6],[3,5,7,6],[3,7,3,1]]
print(maks_iloraz(T))
