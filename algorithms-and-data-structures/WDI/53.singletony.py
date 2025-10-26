def is_singleton(num,T): #num i T to tablica T2
    n = len(T)
    flag = False
    for i in range(n):
        for j in range(n):
            if(T[i][j] == num and not flag): flag = True #not flag to inaczej flag == False
            elif(T[i][j] == num and flag): return False
    return True

def push(T,num,i): #przepychanie
    n = len(T)
    temp = T[i]
    T[i] = num
    for j in range(i, n-1):
        T[j+1], temp = temp, T[j+1]

def pseudosort(T,num):
    n = len(T)
    i = 0
    while T[i] < num: #znajduje na którym indeksie umieścić kolejną
        if T[i] == 0:
            T[i] = num
            return
        i+=1
    if i == n-1:
       T[i] = num
    else:
        push(T,num,i)

def zad6(T1):
    n = len(T1)
    T2 = [0 for _ in range(n*n)]
    for i in range(n):
        for j in range(n):
            if is_singleton(T1[i][j], T1):
                pseudosort(T2,T1[i][j])
    return T2

T1 = [[1, 2, 4, 6],
      [4, 10, 15, 20],
      [2, 4, 80, 102],
      [423, 513, 951, 999]]
#T1 = [[12,7,5],[5,8,6],[7,9,1]]
print(zad6(T1))


"""from math import inf
def find_row(T, ixs):
    result = 0
    for i in range(1, len(T)):
        if T[i][ixs[i]] < T[result][ixs[result]]:
            result = i
    return result #zwraca który element wyżej jest mniejszy od obecnego
def zad6(T1, T2):
    n = len(T1)
    ixs = [0 for _ in range(n)]
    prev = -1
    T2_i = 0
    i = 0
    while i < n * n:#ma wypełnić tablicę od 0...n^2 - 1
        row = find_row(T1, ixs) #porównuje czy któryś już nie był taki sam
        if T1[row][ixs[row]] != prev:#jak wyraz nie jest taki sam jak poprzedni
            prev = T2[T2_i] = T1[row][ixs[row]]#to do nowej tablicy na kolejne
            T2_i += 1#indeksy wpisujemy te liczby co jeszcze ich nie było
        if ixs[row] == n - 1:
            T1[row][ixs[row]] = inf #powoduje że już nigdy nie cofniemy
            #się żeby szukać powyżej danego wiersza
        else:
            ixs[row] += 1#stąd potem bierzemy kolejne elementy z wierszy
        i += 1
    return T2

T1 = [[1, 2, 4, 6],
      [4, 10, 15, 20],
      [2, 4, 80, 102],
      [423, 513, 951, 999]]
T2 = [0] * 16
print(zad6(T1, T2))"""