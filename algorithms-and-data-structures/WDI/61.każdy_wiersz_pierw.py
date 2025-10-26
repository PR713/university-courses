
def pierwsza(x):
    if x < 2: return False
    if x == 2 or x == 3: return True
    if x % 2 == 0 or x % 3 == 0: return False
    i = 5
    while i * i <= x:
        if x % i == 0: return False
        i += 2
        if x % i == 0: return False
        i += 5
    return True

def wiersz(tab):
    n = len(tab)
    cnt = 0
    for i in range(n):
        flag_wiersz = 0
        for j in range(n):
            flag = 1
            while tab[i][j] > 0:
                if pierwsza(tab[i][j]%10) == False:
                    flag = 0
                    break#sprawdzamy kolejne
                tab[i][j] //= 10
            if flag: #czyli niezmieniona równa 1 - tzn nie zrobiło break w while
                flag_wiersz = 1
                break
        if flag_wiersz == 0: return False
    return True

tab = [[1, 23, 1, 4],
       [2, 2, 4, 2],
       [9, 6, 7, 8],
       [26, 7, 5, 3]]
print(wiersz(tab))





