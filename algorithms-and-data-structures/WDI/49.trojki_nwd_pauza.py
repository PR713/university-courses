
def nwd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def trojki(tab):
    n = len(tab)
    cnt = 0
    for i in range(n - 2):
        if nwd(nwd(tab[i], tab[i + 1]), tab[i+2] ) == 1:
            cnt += 1
    for i in range(n-3):
        if nwd(nwd(tab[i], tab[i+1]), tab[i+3]) == 1:
            cnt += 1
        if nwd(nwd(tab[i], tab[i+2]), tab[i+3]) == 1:
            cnt += 1
    for i in range(n-4):
        if nwd(nwd(tab[i], tab[i + 2]), tab[i + 4]) == 1:
            cnt += 1
    return cnt

tab = [1,2,3,4,5]
print(trojki(tab))
