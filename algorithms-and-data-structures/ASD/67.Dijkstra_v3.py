from math import inf
from queue import PriorityQueue

def Dijkstra(G, start):
    n = len(G)
    d = [inf for _ in range(n)]
    par = [None for _ in range(n)]
    d[start] = 0
    Q = PriorityQueue()
    Q.put((0, start))
    while not Q.empty():
        w, u = Q.get()
        if w == d[u]:  # tylko wchodzimy do fora gdy wchodzimy
            # tą najkrótszą ścieżką, nie ma sensu sprawdzać relaksacji
            # dla jakichś dłuższych, a krótszych nie będzie bo d[u] jest
            # najkrótsze, nie ma sensu sprawdzać od innych wierzchołków
            #bo poprzednie kopie nadal są w kolejce i żeby potem nie brać
            #tych coraz większych bo bez sensu, pesymistycznie put i get
            #to O(log(V^2)) = O(logV) i tak
            for v, c in G[u]:
                if relax(par, d, v, c, u):
                    Q.put((d[v], v))
    return d, par

def relax(par, d, v, c, u):
    if d[v] > d[u] + c:
        d[v] = d[u] + c
        par[v] = u
        return True
    return False

G = [[(1, 3), (6, 2)],
    [(0, 3), (2, 2), (8, 1)],
    [(1, 2), (3, 5)],
    [(4, 20), (2, 5), (8, 1)],
    [(5, 8), (3, 20), (7, 2)],
    [(6, 3), (7, 1), (4, 8)],
    [(0, 2), (7, 1), (5, 3)],
    [(6, 1), (5, 1), (8, 7), (4, 2)],
    [(7, 7), (1, 1), (3, 1)]]

print(Dijkstra(G,0))


######################
from queue import PriorityQueue
def Dijkstra(G, start):
    n = len(G)
    d = [float('inf') for _ in range(n)]
    par = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    d[start] = 0
    Q = PriorityQueue()
    Q.put((0, start))
    while not Q.empty():
        w, u = Q.get()

        if visited[u]: continue

        for v, c in G[u]:
            if relax(par, d, v, c, u):#tu nie trzeba
    #not visited bo skoro był już zdjęty to relax i tak
    #nie przepuści
                Q.put((d[v], v))
        visited[u] = True
    return d, par


