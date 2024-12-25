
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

#####################################################

from queue import PriorityQueue

#O(ElogV + V), Dijkstra + lista O(V)
def dijsktra(G, start):
    dist = [float('inf') for _ in range(len(G))]
    dist[start] = 0
    q = PriorityQueue()
    q.put((0, start))
    while not q.empty():
        time, cur = q.get()
        if dist[cur] != time: continue

        for edge, weight in G[cur]:
            if time + weight < dist[edge]:
                dist[edge] = time + weight
                q.put((dist[edge], edge))
    return dist


def spacetravel(n, E, S, a, b):
    Os = [False for _ in range(n)]
    for s in S:
        Os[s] = True

    G = [[] for _ in range(n + 1)]
    for v, u, w in E: #jeden duży wierzchołek, jest od 0...n-1 ich
    #a n-ty to też duży zrobimy ale też O(ElogV + S)
        if Os[v] and Os[u]:
            continue
        elif Os[v]:
            G[n].append((u, w))
            G[u].append((n, w))
        elif Os[u]:
            G[n].append((v, w))
            G[v].append((n, w))
        else:
            G[v].append((u, w))
            G[u].append((v, w))

    dist = dijsktra(G, a if not Os[a] else n)
    return dist[b if not Os[b] else n]


