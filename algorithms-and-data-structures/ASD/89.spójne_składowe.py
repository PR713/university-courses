
#w nieskierowanym ile spójnych składowych

def DFS(G):
    def dfs_visit(G,s):
        visited[s] = True
        for v in G[s]:
            parent[v] = u
            dfs_visit(G, v)

    n = len(G)
    cnt = 0
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            dfs_visit(G,u)
            cnt += 1 #licznik spójnych składowych
    return cnt


