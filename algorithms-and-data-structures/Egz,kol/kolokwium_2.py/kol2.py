#Radosław Szepielak
#Algorytm szukania ile trwa najszysza droga wojownika z 's' do 't'
#opiera się na zamianie grafu G - listy krawędzi, na listę sąsiedztwa.
#Używam tutaj zmodyfikowanej Dijkstry, pod kątem listy dystansów 'dist',
#która ma 17 pól od 0,...,16 dla każdego wierzchołka, mówiących nam o tym
#z jakim zmęczeniem najmniejszym do tej pory dotarto do danego wierzchołka.
#W kolejce priorytetowej przechowuję trzy wartości, najkrótszą drogę ze
#zmęczeniem time, time oraz wierzchołek do którego dotarliśmy w ten sposób.
#Jeśli czas zmęczenia 'time' + waga krawędzi do następnego wierzchołka
#przekracza 16, to sprawdzam czy jeśli wojownik odpocznie w 'u', a następnie
#wyruszy do niego idąc krawędzią o wadze 'val', to czy docierając ze zmęczeniem
#'val' do 'v' czy będzie to lepszym rezultatem od dotychczasowych.
#W drugim przypadku jeśli jeszcze nie wyczerpał czasu <= 16 godzin wędrówki,
#to analogicznie sprawdzam czy dojście ze zmęczeniem większym o 'val',
#będzie bardziej optymalne niż poprzednie dotarcie. Jeśli dotarliśmy do 't'
#zwracamy wartość najszybszej drogi wojownika.
#Złożoność czasowa O(ElogV)
#Złożoność pamięciowa O(V+E)


from kol2testy import runtests
from queue import PriorityQueue

def edges_to_adjacency(G):
    n = max(max(u, v) for u, v, _ in G) + 1 #liczba wierzchołków, O(E)
    new_G = [[] for _ in range(n)]
    for e in G: #O(E)
        u, v, w = e
        new_G[u].append((v, w))
        new_G[v].append((u, w))
    return new_G

def warrior(G, s, t):
    Graph = edges_to_adjacency(G)  # O(E+V)
    n = len(Graph)
    Q = PriorityQueue()
    dist = [[float('inf') for _ in range(17)] for _ in range(n)]
    dist[s][0] = 0  # w pełni wypoczęty ruszając z 's'
    Q.put((0, 0, s))  # droga, zmęczenie, wierzchołek
    while not Q.empty():
        w, time, u = Q.get()
        if w == dist[u][time]: #żeby nie wyjmować potencjalnych słabszych
            # kopii z danym zmęczeniem ale gorszym czasem wędrówki 'w'
            if u == t: return w #szukana liczba godzin wędrówki wojownika
            for v, val in Graph[u]:
                if time + val > 16:  # musi iść odpocząć
                    if dist[v][val] > dist[u][time] + 8 + val:
                        dist[v][val] = dist[u][time] + 8 + val
                        Q.put((dist[v][val],val,v))
                else: #może jeszcze iść <= 16
                    if dist[v][time + val] > dist[u][time] + val:
                        dist[v][time + val] = dist[u][time] + val
                        Q.put((dist[v][time + val], time + val, v))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
