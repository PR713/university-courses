def ruch(T,row,col,cnt = 1):
    n = len(T)
    T[row][col] = cnt
    if cnt == n**2:
        for j in T:
            print(j)
        exit()
    else:
        for i in range(8):
            if r:= move(T,row,col,i):
                ruch(T,r[0],r[1],cnt +1)
            #end for,,,#jeśli chcemy się cofnąć bo już nie można wykonać
        T[row][col] = 0 #ruchu to pole wyzerować i wykona się to gdy nie
        # będzie można wykonać żadnego z 8 ruchów, tzn rekurencja się cofnie
        # i przejdzie na inne pole a to zostawi wolne

def move(T,row,col,i):
    n = len(T)
    dx = (1,2,2,1,-1,-2,-2,-1)
    dy = (-2,-1,1,2,2,1,-1,-2)
    n_row = row + dy[i]
    n_col = col + dx[i]
    if 0 <= n_row < n and 0<= n_col < n and T[n_row][n_col] == 0: #czyli
        #tablica T od początku wypełniona zerami i można się tam ruszyć
        return n_row, n_col
    return False

n = int(input("Podaj wymiary szachownicy: "))
T = [[0 for _ in range(n)] for _ in range(n)]
ruch(T,0,0) #np z pola (0,0) zaczynamy
