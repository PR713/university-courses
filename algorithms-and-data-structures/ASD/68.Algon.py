
from queue import PriorityQueue
#działa gorzej niż 69
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

    def dijkstra(G, s, e):
        n = len(G)
        inf = float('inf')
        weights = [inf] * n
        to_relax = n
        Q = PriorityQueue()
        Q.put((0, s))
        while not Q.empty() and to_relax:
            min_w, u = Q.get()
            if min_w < weights[u]:
                weights[u] = min_w
                to_relax -= 1
                if u == e: break
                for v, weight in G[u]:
                    if weights[v] == inf:
                        Q.put((weights[u] + weight, v))

        return weights[e]

    G = neighbours(n, E, S)
    t = dijkstra(G,a,b)
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