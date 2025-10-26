from kol3btesty import runtests

from queue import PriorityQueue


def add_edges(G,A):
    n = len(G)
    #for i in range(n): #9.5 s
    #    for j in range(n):
    #        if i != j:
    #            G[j].append((i,A[j]+A[i]))
    G.append([]) #0.04s
    for i in range(n):
        G[i].append((n, A[i]))
        G[n].append((i, A[i]))
    return G

def Dijkstra(G,s,t):
    n = len(G)
    d = [float('inf') for _ in range(n)]
    Q = PriorityQueue()
    Q.put((0,s))
    d[s] = 0
    while not Q.empty():
        w,u  = Q.get()
        if u == t: return d[u]
        if w == d[u]:
            for v,val in G[u]:
                if d[v] > d[u] + val:
                    d[v] = d[u] + val
                    Q.put((d[v],v))
    return None


def airports(G,A,s,t):
    G = add_edges(G,A)
    return Dijkstra(G,s,t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )