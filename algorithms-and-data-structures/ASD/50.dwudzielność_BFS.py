from collections import deque

#lista sąsiedztwa
def dwudzielnosc(G):
    n = len(G)
    colors = [-1 for _ in range(n)]
    Q = deque()
    Q.append(0)
    colors[0] = 0
    while len(Q) > 0:
        u = Q.popleft() #jako kolejka
        for v in G[u]:
            if colors[v] == -1:
                colors[v] = (colors[u] + 1) % 2
                Q.append(v)
            elif colors[v] == colors[u]:
                return False
    return True