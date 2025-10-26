from kol2testy import runtests

def adjacency_to_edges(G):
    n = len(G) # [[(0,1)], []...]
    new_G = []
    for i in range(n):
        for v,w in G[i]:
            if i < v:
                new_G.append((i,v,w))
    return new_G

def edges_to_adj(G,n):
    new_graph = [[] for _ in range(n)]
    for e in G:
        new_graph[e[0]].append((e[1],e[2]))
        new_graph[e[1]].append((e[0],e[2]))
    return new_graph

def DFS(G):
    n = len(G) #adj
    visited = [False for _ in range(n)]
    cnt = 0
    for v in range(n):
        if not visited[v]:
            DFSvisit(G,v,visited)
            cnt += 1
        if cnt == 2: return False
    return True

def DFSvisit(G,s,visited):
    visited[s] = True
    for u,w in G[s]:
        if not visited[u]:
            DFSvisit(G,u,visited)

def beautree(G):
    V = len(G)
    G = adjacency_to_edges(G)
    G = sorted(G, key=lambda d: d[2])
    E = len(G)
    suma = float('inf')
    if E < V - 1: return None
    for i in range(E-V): #O(E)
        end = i+V-1
        edges = G[i:end] #O(V)
        Graph = edges_to_adj(edges,V) #V-1 krawędzi, V wierzchołków
        #czyli DFS ma O(V+V) = O(V)
        if DFS(Graph): #czyli n-1 krawędzi i spójny czyli MST
            sum_tmp = 0
            for j in edges:
                sum_tmp += j[2]
            if sum_tmp < suma:
                suma = sum_tmp
    return suma if suma != float('inf') else None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
