
#Znaleźć najkrótsze ścieźki z 's' do pozostałych
#wierzchołków w DAG
#sortowanie topologiczne 59. + relaksacja krawędzi (1 iteracja Bellman)
#O(V+E) - liniowe topologiczne sortowanie (to DFS) i przejście z relaksacją
#które też jest liniowe O(E) bo każda krawędź jest raz relaksowana.
# O(V) * O(e) = O(E), O(e) to krawędzie wychodzące z danego 'u'.

#a Dijkstra to byłoby O(ElogV), while wykonywany O(V) razy,
#operacja q.get O(logV), q.put O(logV), for v, w in G[u] O(e),
#zatem O(V*(logV + O(e)*logV)) = O((V+E)*logV) = O(ElogV)

#Dijkstra z kopcem Fibonacciego O(V*(logV + O(e)*O(1)) = O(VlogV + E)

#DFS/ BFS to V*(O(1)+O(e)) = O(V+E)
#DFS rekurencyjnie wywołujemy, ale jeśli not visited
#więc analiza sumaryczna daje to samo, dla każdego wierzchołka
#robimy relaksację wychodzących z niego O(e) krawędzi

def top_sort(G):
    visited = [0] * len(G)
    A = []
    def visit(G, v, A):
        nonlocal visited  # listy są modyfikowalne
        # tylko zmienne trzeba nonlocal
        visited[v] = 1
        for u in G[v]:
            if not visited[u[0]]:
                visit(G, u[0], A)
        A.append(v) #lub idx = len(G), i A[idx] = v, idx -= 1
        #i bez odwracania potem

    for i in range(0, len(G)):
        if not visited[i]:
            visit(G, i, A)

    return A[::-1]  # trzeba odwrócić


def short_dag(G,s):
    weights = [float('inf') for _ in range(len(G))]
    parents = [None for _ in range(len(G))]
    G_top = top_sort(G)
    weights[s] = 0
    s_id = G_top.index(s) #pobieramy indeks 's' w tablicy DAG'a
    for i in range(s_id,len(G)): #lub dla wszystkich, for u in G_top:
        #ale wcześniejszych nie trzeba bo do nich nie ma krawędzi
        #bo są przed wierzchołkiem w tablicy DAG'a
        u = G_top[i]
        for v, w in G[u]:
            if weights[v] > weights[u] + w:
                weights[v] = weights[u] + w
                parents[v] = u

    return parents,weights


G = [[(1, 3), (6, 2)],
    [(0, 3), (2, 2), (8, 1)],
    [(1, 2), (3, 5)],
    [(4, 20), (2, 5), (8, 1)],
    [(5, 8), (3, 20), (7, 2)],
    [(6, 3), (7, 1), (4, 8)],
    [(0, 2), (7, 1), (5, 3)],
    [(6, 1), (4, 2)],
    [(7, 7), (1, 1), (3, 1)]]
print(short_dag(G,3))
#bez u = G_top, tylo potem for v,w in G[i] jeśli result/G_top
#nie ma po kolei 1,2,3... nie zadziała np tutaj G=^