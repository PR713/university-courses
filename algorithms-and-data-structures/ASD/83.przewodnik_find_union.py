
#przewodnik turystyczny z find union
#Kruskal ale z wagami od największych do najmniejszych
#z miasta A do B
#sort(G, reversed = True)
#while find(A) != find(B):
#    union(A,C), min = 100
#    union(B,D), min = 90
#    union(C,D), min = 20

#Chcemy znaleźć maksymalną przepustowość.
#Pomysł: używamy Kruskala, ale znajdujemy
#"maksymalne" drzewo rozpinające, aż nie
#połączą się wierzchołki s i k.

from math import inf
from math import ceil
from queue import PriorityQueue

class Node:
    def __init__(self, id_):
        self.id = id_
        self.parent = self
        self.rank = 0  # The upper tree's height limit

def find(x: 'Node object') -> 'set representative id':
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x: 'Node object', y: 'Node object'):
    x = find(x)
    y = find(y)
    if x == y: return

    if x.rank < y.rank:
        x.parent = y
    else:
        y.parent = x
        if x.rank == y.rank: x.rank += 1

def kruskal(E,n):
    E = sorted(E, key = lambda d: d[2], reverse=True)#od największych
    A = []
    V = [Node(i) for i in range(n)]

    for e in E: #zakładamy że spójny, i drzewo zawrze wszystkie n
        # wierzchołków a długość ścieżki to n-1
        u,v,w = e
        if find(V[u]) != find(V[v]):
            union(V[u],V[v])
            A += [e]
    return A

def Dijkstra(G,s):
    n = len(G)
    d = [inf for _ in range(n)]
    par = [None for _ in range(n)]
    d[s] = 0
    Q = PriorityQueue()
    Q.put((s,0))
    while not Q.empty():
        v,w = Q.get()
        if w == d[v]: #żeby starych kopii nie brać
            for u,c in G[v]:
                if d[u] > d[v] + c:
                    d[u] = d[v] + c
                    Q.put((u,d[u]))
                    par[u] = v
    return par, d

def Transport(E,s,k,n,m): #n liczba osób
    E = kruskal(E,m) #maksymalne drzewo
    G = [[] for _ in range(m)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
        G[e[1]].append((e[0], e[2])) #reprezentacja listowa
        #z krawędziami tylko z maksymalnego drzewa :O

    par, d = Dijkstra(G, s) #Dijkstra w drzewie <3
    path = []
    t = k
    while t != None:
        path.append(t)
        t = par[t]
    path.reverse()
    mini = d[path[1]] - d[path[0]]
    for i in range(1, len(path) - 1):
        a = d[path[i + 1]] - d[path[i]] #dlatego że to drzewo, to
#różnica między następnymi na ścieżce to waga krawędzi między nimi
#czyli to ile osób można przewieźć najmniej szukamy jakąś krawędzią
        if mini > a: mini = a
    return path, mini, ceil(n / mini)

E=[(0,1,25),(0,2,50),(1,0,25),(1,2,10),(1,3,50),(2,0,50),(2,1,10),
(2,3,20),(3,1,50),(3,2,20),(3,4,9),(3,5,7),(3,6,15),(4,3,9),(4,5,11),
(4,6,14),(5,3,7),(5,4,11),(5,6,10),(6,3,15),(6,4,14),(6,5,10)]
print(Transport(E,0,5,100,7))
E=[(0,1,17),(0,2,31),(0,3,11),(1,0,17),(1,2,19),(1,3,25),
(2,0,31),(2,1,19),(2,4,15),(3,0,11),(3,1,25),(3,4,13),
(3,5,7),(4,2,15),(4,3,13),(4,5,14),(5,3,7),(5,4,14)]
print(Transport(E,0,5,300,6))
E=[(0,1,12),(0,2,12),(0,3,10),(1,0,12),(1,2,8),(1,4,15),(2,0,12),(2,1,8),
(2,3,4),(2,4,7),(3,0,10),(3,2,4),(3,4,11),(4,1,15),(4,2,7),(4,3,11)]
print(Transport(E,3,2,50,5))
