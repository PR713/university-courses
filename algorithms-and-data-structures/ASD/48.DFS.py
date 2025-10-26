
def DFS(G,s):
    visited = [False] * len(G)
    parent = [None] * len(G)
    def dfs_visit(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(G,v)

    dfs_visit(G,s)
    #lub DFS(G) i for u in range(len(G)):
    #               if not visited[u]:
    #                   dfs_visit(G,u)
    #jeśli spójny to raz się wywoła dfs_visit,
    #jeśli niespójny to kilka razy
    #lub spójność if False in visited: return ("nie spójny")
    #
    return visited, parent

G = [[1],[0,2],[1,3,4],[2,4,5],[2,3],[3]] #spójny
#G = [[1],[0,2],[1,3,4],[2,4,5],[2,3],[3],[7],[6]] #niespójny
print(DFS(G,0))