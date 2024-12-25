#każde miasteczko z murem, N,S bramami
#goniec wchodzi jedną to wychodzi drugą
#drogi nie łączą miast bezpośrednio tylko przez oazy
#z jednej bramy wychodzi jedna droga do jakiejś oazy
#(do oazy dowolnie wiele dróg, oazy mogą się łączyć
#między sobą)
#graf spójny i oazy nie są liściami
#goniec ma odwiedzić wszystkie miasta, każde miasto
#dokładnie raz (i to nie Cykl Hamiltona XD)
#coś w stylu cyklu Eulera
#przekształcenie grafu + Cykl Eulera
#każde z miast potraktować jako krawędź,
#A,B,C łączą oazy 1,2,3, jeśli dwie oazy
#połączone to możemy je traktować jako jedną oazę
#czy stopień każdego wierzchołka jest parzysty...
#możemy otrzymać multigraf

##############################################
"""
Oazy i miasta
mamy panstwo

te miasta maja bramy na polnocy i poludniu
miedzy miastami znajduja sie oazy
z miast wychodza drogi na polnoc i poludnie i przechodzi przez jakies oazy
w reulach panstwa, w przypadku wjazdu do miasta jedna bramu, musimy wyjechac druga
istnie problem, bo mamy czlowieka, ktory chce odwiedzic wszystkie miasta dokladnie raz
jesli goniec wjedzie od polnocy, to musi wyjechac od poludnia
wyjezdza ze stolicy i wraca do stolicy druga droga.

narzuca sie ze miasto to krawedz skierowana, w dwie strony, a cala ta przestrzeń ( te krawedzie ) zamienic na wierzcholek
mamy wiec problem znalezienia cykl eulera, a nie cyklu hamiltona.
nie musza byc jednak krawedzie skierowane

jak zamienic krawedzie ( te oazy, te duze przestrzenie ) na wierzcholek


"""
# tablica, ktore wierzcholki to miasta
# tablica, ktora mowi, ktore miasto odwiedzilismy

from collections import deque

def createG(n, edges):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a = edge[0]
        b = edge[1]
        G[a].append(b)
        G[b].append(a)

    return G


def DFS(G, cities, visited, visitedCities, v):
    visited[v] = True

    for neighbour in G[v]:

        if cities[neighbour]:
            visitedCities.append(neighbour)
            visited[neighbour] = True

        elif visited[neighbour] == False:
            DFS(G, cities, visited, visitedCities, neighbour)


def createNewGraph(G, cities):
    n = len(G)
    visited = [ False for _ in range(n) ]
    newG = [ [] for _ in range(n) ]
    visitedCities = []

    for v in range(n):

        if visited[v] == False and cities[v] == False:
            DFS(G, cities, visited, visitedCities, v)

            newG[v] = visitedCities
            for k in visitedCities:
                newG[k].append(v)

            visitedCities = []

    return newG


def OasisAndCities(G, listOfCities):

    n = len(G)
    adjacencyMatrix = [ [ 0 for _ in range(n) ] for _ in range(n) ]
    visited = [ False for _ in range( len(G) ) ]
    cities = [ False for _ in range(n) ]

    for v in listOfCities:
        cities[v] = True

    G = createNewGraph(G, cities)
    n = len(G)
    print(G)
    for v in range(n):
        if visited[v] == False and cities[v] == False and len( G[v] ) > 0:
            BFS(G, visited, adjacencyMatrix, v)
    #
    newGraph = transformGraph( adjacencyMatrix )
    return newGraph


def BFS(G, visited, adjacencyMatrix, vertex):
    queue = deque()
    queue.append(vertex)
    visited[vertex] = True

    while queue:
        s = queue.popleft()

        for neighbour in G[s]:
            adjacencyMatrix[neighbour][s] = 1


def transformGraph( adjMatrix ):
    n = len( adjMatrix )
    G = [ [] for _ in range(n) ]

    for y in range(n):
        a = -1
        b = -1
        for x in range(n):
            if adjMatrix[y][x] == 1 and a == -1:
                a = x
            elif adjMatrix[y][x] == 1:
                b = x

        if a != -1 and b != -1:
            G[a].append(b)
            G[b].append(a)
    return G

listOfCities = [0, 5, 6, 10]

edges = [ (0, 1), (1, 2), (2, 4), (3, 4), (3, 5), (5, 7), (7, 8), (8, 9), (4, 6), (6, 9),
         (10, 11), (11, 12), (12, 13), (13, 0), (1, 3), (8, 10) ]

G = createG(14, edges)
newG = OasisAndCities(G, listOfCities)
print( newG )
# na koniec sprawdz cykl Eulera