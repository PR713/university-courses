from egz1Atesty import runtests
from queue import PriorityQueue
#O(ElogV) = O(V^2*logV)
def Dijkstra(G,s):
    n = len(G)
    d = [float('inf') for _ in range(n)]
    d[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))
    while not Q.empty():
        w, u = Q.get()
        if w == d[u]:
            for v, c in G[u]:
                if d[v] > d[u] + c:
                    d[v] = d[u] + c
                    Q.put((d[v], v))
    return d

def Dijkstra2(G,s,r):
    n = len(G)
    d = [float('inf') for _ in range(n)]
    d[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))
    while not Q.empty():
        w, u = Q.get()
        if w == d[u]:
            for v, c in G[u]:
                if d[u] + c * 2 + r < d[v]:
                    d[v] = d[u] + c * 2 + r
                    Q.put((d[v], v))
    return d

def gold(G, V, s, t, r):
    first = Dijkstra(G,s)
    second = Dijkstra2(G,t,r) #z t do innych najkrótsze
    #po podwojonych  + r
    n = len(G)
    res = float('inf')
    for i in range(n):
        res = min(res, first[i] + second[i] - V[i])
    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests= True)
