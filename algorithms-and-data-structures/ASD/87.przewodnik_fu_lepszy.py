class Union_Find:
    def __init__(self, n):
        self.p = [i for i in range(n)] #parents każdy swoim na początku
        self.s = [0 for _ in range(n)] #każdy zbiór ma po jednym
        #wierzchołku, a rank ma liczbę poziomów w drzewie

    def Find(self, a):
        if self.p[a] == a: return a
        self.p[a] = self.Find(self.p[a])
        return self.p[a]

    def Union(self, a, b):
        a = self.Find(a)
        b = self.Find(b)
        if a == b: return

        if self.s[a] < self.s[b]:
            a, b = b, a

        self.p[b] = a
        self.s[a] += self.s[b] #dodaje liczbę elementów


def zad4(E, A, B, K):  # O(ElogE) [ https://stackoverflow.com/questions/20432801/time-complexity-of-the-kruskal-algorithm ]
    n = 0
    for a, b, c in E:
        n = max(n, a + 1, b + 1) #liczba wierzchołków

    E.sort(key=lambda x: x[2], reverse=True)
    UF, Tree = Union_Find(n), [[] for _ in range(n)]
    #Tree to lista sąsiedztwa

    # Maksymalne drzewo rozpinające (Algorytm Kruskala)
    for a, b, c in E:
        if UF.Find(a) != UF.Find(b):
            UF.Union(a, b)
            Tree[a].append((b, c))
            Tree[b].append((a, c))

    path = []

    def dfs(n, p=-1, mn=float('inf')):
        path.append(n)
        if n == B: return mn
        #p parent, początkowo -1
        for e, w in Tree[n]: #w liście sąsiedztwa
            if e != p:
                tmp = min(mn, w)
                ans = dfs(e, n, tmp)
                if ans: return ans

        path.pop() #jeśli nie znaleziono to wywalamy z listy od końca
        #w rekurencji i patrzymy na inne modyfikując ją
        return False

    mn = dfs(A)
    return (K + mn - 1) // mn, path

E=[(0,1,25),(0,2,50),(1,0,25),(1,2,10),(1,3,50),(2,0,50),(2,1,10),
(2,3,20),(3,1,50),(3,2,20),(3,4,9),(3,5,7),(3,6,15),(4,3,9),(4,5,11),
(4,6,14),(5,3,7),(5,4,11),(5,6,10),(6,3,15),(6,4,14),(6,5,10)]
print(zad4(E,0,5,100))
E=[(0,1,17),(0,2,31),(0,3,11),(1,0,17),(1,2,19),(1,3,25),
(2,0,31),(2,1,19),(2,4,15),(3,0,11),(3,1,25),(3,4,13),
(3,5,7),(4,2,15),(4,3,13),(4,5,14),(5,3,7),(5,4,14)]
print(zad4(E,0,5,300))
E=[(0,1,12),(0,2,12),(0,3,10),(1,0,12),(1,2,8),(1,4,15),(2,0,12),(2,1,8),
(2,3,4),(2,4,7),(3,0,10),(3,2,4),(3,4,11),(4,1,15),(4,2,7),(4,3,11)]
print(zad4(E,3,2,50))

#(10, [0, 1, 3, 6, 4, 5])
#(22, [0, 2, 4, 5])
#(5, [3, 4, 1, 0, 2])