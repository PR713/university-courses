
#Graf nieskierowany, wagi N+, znaleźć
#ścieżkę s -> t o minimalnym iloczynie wag
#a*b*c*...
#log(a*b*c*...*n) = loga + logb + ... + logn
#czyli szukamy o najmniejszej sumie teraz :)
#Dijkstrę też można zamiast Bellmana Forda
#
from math import log10
def logi(G): #O(E)
    n = len(G)
    for i in range(n): #O(V)
        for j in range(len(G[i])): #O(e)
            x = G[i][j]
            new = log10(x[1])
            G[i][j] = (x[0],new)

    return G #graf z wagami zlogarytmowanymi
#żeby nie logarytmować w pętli tych samych krawędzi
#wiele razy
#Bellman Ford
def path(G,s,t):
    G = logi(G)
    n = len(G)
    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    d[s] = 0
    for _ in range(n-1):#n-1 bo długość najdłuższej ścieżki
        for v in range(n):
            for u,w in G[v]:
                if d[u] > d[v] + w:
                    d[u] = d[v] + w
                    parent[u] = v
    return parent, d[t]

graph = [[(1, 20), (2, 30)],
         [(0, 20), (3, 12), (4, 11)],
         [(0, 30), (3, 18), (5, 2700)],
         [(1, 12), (2, 18), (8, 22), ],
         [(1, 11), (6, 15)],
         [(2, 2700), (7, 19), (8, 3)],
         [(4, 15), (8, 8)],
         [(5, 19)],
         [(3, 22), (5, 3), (6, 8)]]

u, v = 0, 7
print(path(graph,0,7))

#lub można zwykłą Dijkstrę na grafie zlogarytmowanym :)