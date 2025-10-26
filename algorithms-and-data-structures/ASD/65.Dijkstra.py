from queue import PriorityQueue
#O(ElogV)
def Dijkstra(G,s):#,e): jeśli chcemy ustalić cel to dodatkowy
    #argument 'e'
    n = len(G)
    parent = [None] * n
    distance = [float("inf")]*n
    Q = PriorityQueue()
    distance[s] = 0
    Q.put((0,s)) #waga, wierzchołek
    while not Q.empty():
        u = Q.get()[1] #PriorityQueue w ten sposób wyciągamy
        #element o najniższym priorytecie, czyli najmniejszej wartości
        #distance[u], trochę jak struktura Heapmin
        #ALE TRZEBA if w == d[u]: żeby nie brać starych kopii
        #z kolejki, bo bez tego mamy O(V^2 * (logV + elogV))=O(VElogV)
        for v, w in G[u]:#relaksacja dla każdej krawędzi z u do v
            if distance[v] > distance[u] + w:
                distance[v] = distance[u]+w
                parent[v] = u
                Q.put((distance[v],v))
            #if u == e: #e ostatni wierzchołek
            #    return distance[u]
    return distance, parent

G = [[(1, 3), (6, 2)],
    [(0, 3), (2, 2), (8, 1)],
    [(1, 2), (3, 5)],
    [(4, 20), (2, 5), (8, 1)],
    [(5, 8), (3, 20), (7, 2)],
    [(6, 3), (7, 1), (4, 8)],
    [(0, 2), (7, 1), (5, 3)],
    [(6, 1), (5, 1), (8, 7), (4, 2)],
    [(7, 7), (1, 1), (3, 1)]]

print(Dijkstra(G,0))