#pełny Bellman Ford
#najlepszy korzeń
#dane jest ważone drzewo T. Znajdź s w T
#takie, że odległość od s do najdalszego
#wierzchołka jest minimalna
#O(V) bo drzewo

#dwa DFS'y/BFS'y, raz z dowolnego i najdalszy to A
#DFS z A i znajdujemy najdalszy czyli B,
# A i B to końce średnicy
#w forze if not visited: robimy d[v] = d[u] + w
#(lub na poczatku funkcji przed forem ale trzeba
#pamiętać w czym się przed wywołaniem było, bez sensu)
#tylko dlatego, że to jest drzewo to robiąc tak
#na pewno nie będzie innej krótsze/dłuższej ścieżki,
#bo nie ma innego dojścia do wierzchołka niżej!!
#BFS z A i B na raz ale chyba zmodyfikowany (aż się spotkają
#- to jest 's' - na średnicy na pewno bo poza będą gorsi
#kandydaci, bo ich odległości do obu będą większe od tych
#na średnicy, ze względu na strukturę drzewa)
#BFS wagowy zamiast d[v] = d[u] + 1 to d[u] + w)
#nie bo np A-100-100-y-100-x-1-1-1-B, spotkałby się w 'x'
#a powinien w 'y', tylko BFS przesuwający się co 1 jednostkę

#lub wystarczy przejść przez tę ścieżkę, która jest średnicą
#i sprawdzać maksymalną odległość od jednego i drugiego końca
#średnicy dla każdego z wierzchołków, jakie leżą na tej średnicy
#i zapamiętywać ten wierzchołek, dla którego jedna z dwóch odległości
#od końców średnicy jest najmniejsza

#lub dwa razy Dijkstra i szukamy maksymalnej ścieżki z tablicy d,
#potem z tego wierzchołka do którego jest największa znowu Dijkstra
#i coś dzielimy przed dwa dystanse... wiki


#sposób DFS'y, lub BFS'ami akurat dla drzewa działa
def max_val_idx(A):
    max_i = 0
    for i in range(1, len(A)):
        if A[i] > A[max_i]:
            max_i = i
    return max_i

def diam_dist(G: 'undirected weighted acyclic graph represented by adjacency lists'):
    n = len(G)
    inf = float('inf')
    # Find the first diameter end vertex
    dist = [inf] * n
    visited = [0] * n
    token = 1

    def dfs(u):
        visited[u] = token #lub za każdym razem nowa lista visited i dist
        for v, weight in G[u]:
            if visited[v] != token:
                dist[v] = dist[u] + weight
                dfs(v)

    # Find the first diameter end vertex
    dist[0] = 0
    dfs(0)
    diam_u = max_val_idx(dist)

    # Find distances of all vertices from the first diameter end vertex
    # and the second diameter end vertex
    token += 1
    dist[diam_u] = 0
    dfs(diam_u)
    diam_v = max_val_idx(dist)
    dist1 = dist[:]  # Copy all distances from the first diameter vertex

    # Find all distances from the second diameter end vertex
    token += 1
    dist[diam_v] = 0
    dfs(diam_v)
    dist2 = dist[:]  # Copy all distances from the second diameter vertex

    return dist1, dist2


def best_root(G: 'undirected weighted acyclic graph represented by adjacency lists'):
    inf = float('inf')
    #można ewentualnie sprawdzić spójność ale załóżmy że jest spójny
    n = len(G)
    dist1, dist2 = diam_dist(G)
    # Find a vertex of the lowest max dist
    best_u = None
    min_dist = inf #lub chyba jak na wiki różnica między
    #jednym dystansem a drugim //2 najmniejsza czy coś zamiast for
    #to to samo
    for u in range(n):
        max_dist = max(dist1[u], dist2[u])
        if max_dist < min_dist:
            min_dist = max_dist
            best_u = u

    return best_u, min_dist
