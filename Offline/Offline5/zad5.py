#Radosław Szepielak
#Funkcja list_neighbours służy do stworzenia listy sąsiedztwa
#dla krawędzi będących w liście E, a także do dodania wierzchołków
#osobliwości do tej listy sąsiedztwa, o krawędziach z wagą '0'.
#Ponieważ graf jest nieskierowany to musimy dodać zarówno parę
#(u,w) i (v,w), gdzie u jest sąsiadem v, analogicznie z parami
#(S[i],0) oraz (S[j],0). Za pomocą algorytmu Dijkstra, działającym na
#grafie reprezentowanym listą sąsiedztwa z dodatkowymi krawędziami
#z osobliwości, znajdujemy najkrótszy czas podróży z planety a do planety b.


from zad5testy import runtests
from queue import PriorityQueue

def spacetravel( n, E, S, a, b ):
    def list_neighbours(n, G, S):
        lista_sasiedztwa = [[] for _ in range(n)]

        for u, v, w in G:
            lista_sasiedztwa[u].append((v, w))
            lista_sasiedztwa[v].append((u, w))

        s = len(S)
        for i in range(s):
            for j in range(i + 1, s):
                lista_sasiedztwa[S[i]].append((S[j], 0))
                lista_sasiedztwa[S[j]].append((S[i], 0))
        return lista_sasiedztwa

    def Dijkstra(G, a, b):
        n = len(G)
        d = [float('inf')] * n
        Q = PriorityQueue()
        Q.put((0, a))  #waga, wierzchołek
        d[a] = 0
        while not Q.empty():
            u = Q.get()[1]  #z krotki wyciągamy drugi element
            #czyli wierzchołek
            if u == b: #czyli dotarliśmy do celu :)
                return d[b]
            for v, w in G[u]:  #relaksacja dla każdej krawędzi z u do v
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    Q.put((d[v], v))
        return d[b]

    G = list_neighbours(n, E, S) #Graf repr. listą sąsiedztwa z dodatkowymi
    #krawędziami z osobliwości
    t = Dijkstra(G,a,b)
    return t if t != float('inf') else None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )