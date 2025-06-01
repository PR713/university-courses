def pierwsza(x):
    if x < 2: return False
    if x == 2 or x == 3: return True
    if x % 2 == 0 or x % 3 == 0: return False
    i = 5
    while i * i <= x:
        if x % i == 0: return False
        i += 2
        if x % i == 0: return False
        i += 4
    return True

def cyfry(a):
    digit = [False]*10
    while a > 0:
        digit[a%10] = True #liczymy czy wystąpiła czy nie
        #nie krotność bo nie o to chodzi, ma być min. jedna cyfra
        #która jest pierwsza
        a //= 10
    return digit

def wiersz(tab):
    n = len(tab)
    cnt = 0
    for i in range(n):
        for j in range(n):
            digit = cyfry(tab[i][j])
            for k in range(10):
                if digit[k] and pierwsza(k):
                    cnt += 1 #czyli ma min. jedną pierwszą, można break
                    break

            else:
                cnt = 0
                #w tym wierszu przynajmniej jedna tego nie spełnia
    if cnt == n:
        return True
    return False


tab = [[1, 2, 3, 4],
       [2, 3, 4, 9],
       [3, 5, 7, 10],
       [3, 5, 7, 13]]
print(wiersz(tab))
