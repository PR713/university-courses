
#Algorytm Kruskala, G nieskierowany, ważony
#(dane sortowanie i find union)

class Node:
    def __init__(self, id_):
        self.id = id_
        self.parent = self
        self.rank = 0  # The upper tree's height limit

def find(x: 'Node object') -> 'set representative id':
    # If we have to compress a path as we are not a root of a tree
    if x != x.parent:
        # Point all sobsequent nodes on a path to the root node
        x.parent = find(x.parent)
    # Return the current (updated) parent of the node
    #te które były na ścieżce od x do korzenia (kompresja)
    #drzewo staje się coraz bardziej płaskie
    return x.parent

def union(x: 'Node object', y: 'Node object'):
    x = find(x) # Find parents of both x and y
    y = find(y)
    if x == y: return #jeśli są w tym samym zbiorze
    # Otherwise, link the smaller tree to the larger one
    if x.rank < y.rank:
        x.parent = y
    else:
        y.parent = x
        # If both x and y have the same rank and y was linked to x,
        # we have to increase the rank of x
        if x.rank == y.rank: x.rank += 1


def kruskal(E,n): #E - lista krawędzi (u,v,waga), n - liczba krawędzi
    E = sorted(E, key = lambda d: d[2]) #def key(d): return d[2] dla każdej
    #tupli zwraca d[2] i sortuje względem tego
    V = [Node(i) for i in range(n)]
    A = [None for _ in range(n-1)] #minimalne drzewo
    e = i = 0
    while e < n-1: # e - licznik ile krawędzi już mamy
        u1 = V[E[i][0]] #jeden wierzchołek
        u2 = V[E[i][1]] #drugi
        #V[coś] bo przekazujemy Node'a
        if find(u1) != find(u2): #jeśli nie są w tym samym zbiorze
            union(u1,u2) #to je łączymy
            A[e] = E[i]
            e += 1
        i += 1
    return A


E = [(5, 0, 2), (0, 1, 3), (1, 2, 1), (5, 6, 1), (1, 6, 2), (5, 4, 6),
                  (4, 3, 8), (3, 6, 5), (2, 3, 7)]
n = max(max(u,v) for u,v,_ in E) + 1
print(kruskal(E,n))
#[(1, 2, 1), (5, 6, 1), (5, 0, 2), (1, 6, 2), (3, 6, 5), (5, 4, 6)]

#jeśli G jako lista sąsiedztwa, O(V+E), V bo lista długości V,
#fory to O(V*e) = O(E)
#*z listy krawędzi na sąsiedztwa to O(V + E), V bo V list, a E = len(E)
#gdzie E to lista krawędzi których może być E

def graph_(G: 'graph represented using adjacency lists'):
    n = len(G)
    E = []
    V = list(range(n))
    for u in range(n):
        for v, weight in G[u]:
            if v <= u: continue # Avoid repetitions
            E.append((u, v, weight))
    return V, E