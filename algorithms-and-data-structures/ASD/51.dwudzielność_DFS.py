# Implementacja funkcji sprawdzającej czy
# graf jest dwudzielny - bipartited

def bipartited(G):
    n = len(G)
    visited = [0 for _ in range(n)]

    def DFS(v, w):
        visited[v] = w
        for i in G[v]:
            if visited[i] == 0:
                res = DFS(i, -1 * w)
                if not res:
                    return False
            else:
                if visited[i] == w:
                    return False
        return True

    return DFS(0, 1)
#powinno być for v in G: return DFS(v,1) bo może być niespójny
G = [[2,3],[3,4],[0],[0,1],[1]]
print(bipartited(G))
