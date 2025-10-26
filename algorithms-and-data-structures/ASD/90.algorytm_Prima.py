#macierzowo lepiej bez kolejki priorytetowej
#tak samo jak dla Dijkstry :)

from queue import PriorityQueue

def Prim(G,s):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    mins = [float('inf') for _ in range(n)]
    #mins to najmniejsze wagi krawędzi jakimi
    #dostać się można do wierzchołka
    mins[s] = 0
    Q = PriorityQueue()
    Q.put((0,s))
    cnt = 0
    while cnt < n:
        v = Q.get()[1]
        if visited[v]: continue#bo w kolejce może być
    #wiele kopii danego wierzchołka i dodajemy każdą wersję
    #dotarcia z jakąś wagą i z nich minimum przy get()

        for u,w in G[v]:
            if not visited[u] and mins[u] > w: #not visited[u]
    #niezbędne bo jeśli był raz zdjęty, a potem z innego wierzchołka
    #popatrzymy na krawędź jakąś która wchodzi do niego z mniejszą wagą
    #a Prim aktualizuje z bieżącego do sąsiadów, a nie wszystkie wychodzące
    #z danego więc się może to zepsuć w tym przykładzie choćby
                mins[u] = w
                parent[u] = v
                Q.put((w,u))
        visited[v] = True
        cnt += 1
    return parent,mins

G = [[(1,8),(2,5)],[(0,8),(3,3)],[(0,5),(3,2),(4,6)],[(1,3),(2,2),(4,9)],[(2,6),(3,9)]]
print(Prim(G,0))
