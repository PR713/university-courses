
from queue import PriorityQueue
def spacetravel( n, E, S, a, b ):
    def neighbours(n, G, S):
        #n = max(v for _, v, _ in G) + 1
        lista_sasiedztwa = [[] for _ in range(n)]

        for u, v, w in G:
            lista_sasiedztwa[u].append((v, w))
            lista_sasiedztwa[v].append((u, w))

        s = len(S)
        for i in range(s):
            for j in range(i + 1, s):
                lista_sasiedztwa[S[i]].append((S[j], 0))
                lista_sasiedztwa[S[j]].append((S[i], 0))
        return lista_sasiedztwa

    def Dijkstra(G, s,e):
        n = len(G)
        distance = [float("inf")] * n
        Q = PriorityQueue()
        distance[s] = 0
        Q.put((0, s))  # waga, wierzchołek
        while not Q.empty():
            u = Q.get()[1]  # PriorityQueue w ten sposób wyciągamy
            # element o najniższym priorytecie, czyli najmniejszej wartości
            # distance[u], trochę jak struktura Heapmin
            if u == e: #e ostatni wierzchołek
                return distance[e]
            for v, w in G[u]:  # relaksacja dla każdej krawędzi z u do v
                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    Q.put((distance[v], v))

        return distance[e]
    G = neighbours(n, E, S)
    t = Dijkstra(G,a,b)
    return t if t != float('inf') else None


E = [(0,1, 5),
    (1,2,21),
    (1,3, 1),
    (2,4, 7),
    (3,4,13),
    (3,5,16),
    (4,6, 4),
    (5,6, 1)]
S = [ 0, 2, 3 ]
a = 1
b = 5
n = 7
print(spacetravel(n,E,S,a,b))