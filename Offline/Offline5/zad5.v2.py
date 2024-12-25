
from zad5testy import runtests

from queue import PriorityQueue

def spacetravel( n, E, S, a, b ):
    def Dijkstra(G, s):
        n = len(G)
        d = [float('inf')] * n
        Q = PriorityQueue()
        Q.put((0, s))  # waga, wierzchołek
        d[s] = 0
        while not Q.empty():
            u = Q.get()[1]  # z krotki wyciągamy drugi element
            # czyli wierzchołek
            for v, w in G[u]:  # relaksacja dla każdej krawędzi z u do v
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    Q.put((d[v], v))
        return d

    def list_neighbours(n, G):
        lista_sasiedztwa = [[] for _ in range(n)]
        for u, v, w in G:
            lista_sasiedztwa[u].append((v, w))
            lista_sasiedztwa[v].append((u, w))

        return lista_sasiedztwa

    G = list_neighbours(n, E)
    A = Dijkstra(G, a)
    path_a = float('inf')
    s = len(S)
    if s == n: return 0 #czyli wszystkie wierzchołki to osobliwości

    for i in range(s):
        path_a = min(path_a, A[S[i]])
    if path_a > A[b]: #czyli dojście do osobliwości ma wyższy koszt niż bez
        return A[b]

    B = Dijkstra(G, b)
    path_b = float('inf')
    for i in range(s):
        path_b = min(path_b,B[S[i]])

    if A[b] < path_a + path_b:
        return A[b]
    return path_a + path_b if path_a + path_b != float('inf') else None








# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )