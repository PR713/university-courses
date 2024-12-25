
#w 73. był ale bez wykrywania cykli ujemnych
#Złożoność O(VE), bo pierwszy for O(V)
#drugi for O(V), trzeci for O(e) - krawędzie z danego
#O(V*V*e) = O(V*E)

def BellmanFord(G,s):
    n = len(G)
    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    d[s] = 0
    for _ in range(n-1): #n-1 bo długość najdłuższej ścieżki
        for v in range(n):
            for u,w in G[v]:
                if d[u] > d[v] + w:
                    d[u] = d[v] + w
                    parent[u] = v

    for v in range(n):
        for u, w in G[v]:
            if d[u] > d[v] + w: #a powinno być <=
    #bo oznacza że da się zrelaksować (dojść wydajniej) a już
    #sprawdziliśmy wszystkie relaksacje, czyli leży (v,u) leży na
    #cyklu ujemnym
                return False

    return d, parent

G = [[(2,-1)],[(0,-1)],[(1,1)]]
print(BellmanFord(G,0))
