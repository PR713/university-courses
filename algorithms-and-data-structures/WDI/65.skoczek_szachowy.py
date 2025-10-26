def skoczek(tab,iloczyn):
    n = len(tab)
    ile_par = 0
    for i in range(n):
        for j in range(n):
            for (x,y) in ((i+2,j+1),(i+2,j-1),(i+1,j+2),(i-1,j+2),(i-2,j+1),(i-2,j-1),(i-1,j-2),(i+1,j-2)):
                if x < 0 or x > n-1 or y < 0 or y > n-1:
                    continue
                if tab[i][j]*tab[x][y] == iloczyn:
                    ile_par += 1
    return ile_par//2

x = [[1, 1, 1,] for _ in range(3)]
print(skoczek(x, 1))


