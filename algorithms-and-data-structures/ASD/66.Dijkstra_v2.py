from queue import PriorityQueue
#ale chyba mniej wydajny dla rzadkich grafów
#tzn dużo V, mało E, niespójności
def dijkstra(G: 'graph represented by adjacency lists', s: 'source'):#,e):
    n = len(G)
    inf = float('inf')
    weights = [inf] * n
    parents = [None] * n
    # This variable is a counter of vertices remaining which we still
    # have to find shortest paths to
    to_relax = n
    pq = PriorityQueue()
    pq.put((0, s, None))

    while not pq.empty() and to_relax:
        min_w, u, parent = pq.get()
        # We will find the minimum total weight path only once so the
        # code below this if statement will be executed only once
        if min_w < weights[u]: #relaksacja wykonywana tylko raz dla
        #każdego wierzchołka, bo nigdy nie znajdzie jeszcze mniejszego
        #a nie dla wszystkich krawędzi z danego wierzchołka wiele razy
            weights[u] = min_w
            parents[u] = parent
            to_relax -= 1
            #jeśli szukamy do konkretnego wierzchołka to bez to_relax
            #samo if u == e: break
            # Add all the neighbours of the u vertex to the priority queue
            for v, weight in G[u]:
                if weights[v] == inf:
                    pq.put((weights[u] + weight, v, u))

    return weights, parents

G = [[(1, 3), (6, 2)],
    [(0, 3), (2, 2), (8, 1)],
    [(1, 2), (3, 5)],
    [(4, 20), (2, 5), (8, 1)],
    [(5, 8), (3, 20), (7, 2)],
    [(6, 3), (7, 1), (4, 8)],
    [(0, 2), (7, 1), (5, 3)],
    [(6, 1), (5, 1), (8, 7), (4, 2)],
    [(7, 7), (1, 1), (3, 1)]]

print(dijkstra(G,0))