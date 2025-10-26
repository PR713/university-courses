from queue import Queue
from math import inf

def BFS(G,s):
    visited = [False]*len(G)
    parent = [None]*len(G)
    distance = [inf]*len(G)
    Q = Queue()
    visited[s] = True
    distance[s] = 0
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + 1
                Q.put(v)

    return visited, parent, distance

G = [[1],[0,2],[1,3,4],[2,4,5],[2,3],[3]]
#G = [[1],[0,2],[1,3,4],[2,4,5],[2,3],[3],[7],[6]]
#tu tak samo jeśli nie spójny to zostawi False i None
print(BFS(G,0))
