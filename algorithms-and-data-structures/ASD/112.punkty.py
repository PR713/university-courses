#X = {x1,...,xn} zbiór punktów na prostej
#ile min przedziałów jednostkowych trzeba,
#by objąć wszystkie punkty

def points(X):
    n = len(X)
    X.sort()
    pocz = 0
    cnt = 1
    for i in range(1,n):
        if X[pocz] + 1 > X[i]:
            cnt += 1
            pocz = i
    return cnt