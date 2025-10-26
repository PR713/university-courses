def cyfry(x):
    digit = [False] * 10  # cyfry 0,1,...9
    while x > 0:
        digit[x % 10] = True
        x //= 10
    return digit


def przyjaciolki(tab):
    n = len(tab)
    sasiedzi = 0
    for i in range(n):
        for j in range(n):  # bierzemy kolejne elementy
            dig = cyfry(tab[i][j])
            ile = 0
            if i - 1 >= 0:
                if dig == cyfry(tab[i - 1][j]):
                    ile += 1
            if i + 1 <= n - 1:
                if dig == cyfry(tab[i + 1][j]):
                    ile += 1
            if j - 1 >= 0:
                if dig == cyfry(tab[i][j - 1]):
                    ile += 1
            if j + 1 <= n - 1:
                if dig == cyfry(tab[i][j + 1]):
                    ile += 1
            if ile == 4:
                sasiedzi += 1
    return sasiedzi


tab = [
    [1, 6, 3, 4, 18],
    [6, 6, 6, 818, 81],
    [9, 6, 2, 7, 18],
    [4, 5, 7, 7, 5],
    [1, 2, 3, 4, 5]]

print(przyjaciolki(tab))
"""lub po skosie dodatkowo to wtedy (w-1,w+1), (k-1,k+1) bez środka
i sprawdzamy czy cyfry(T[w][k]) jest równe w tych dwóch pętlach
 cyfry(T[w][k])"""
