def binarny(x):
    jedynki = 0
    while x > 0:
       if x % 2 == 1:
        jedynki += 1
       x //= 2
    return jedynki

def tablice(tab1,tab2):
    n1 = len(tab1)
    n2 = len(tab2)
    for i in range(n1-n2+1):
        for j in range(n1-n2+1):
            ile = 0
            for k in range(i,i + n2):
                for l in range(j, j + n2):
                    if binarny(tab1[k][l]) == binarny(tab2[k-i][l-j]):
                        ile += 1
            if ile/(n2*n2) > 1/3: return True
    return False

tab1 =[[1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1]]
tab2 = [[1, 1, 1],
       [0, 0, 0],
       [0, 1, 0]]
print(tablice(tab1,tab2))