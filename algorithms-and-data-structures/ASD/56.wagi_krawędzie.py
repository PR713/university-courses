#każda krawędź ma wagę
#graf skierowany
#możemy tylko iść po malejących wagach
#czy można przejść z jednego wierzchołka do
#drugiego po malejących wagach
#DFS
#trzymamy w visited maksymalne koszty dotarcia
#do danego wierzchołka, więc jeśli następnym
#razem dotrzemy do danego większą wagą
#to zmieniamy pod if'em
#
#lub bez DFS/BFS i posortowania krawędzi i coś

from queue import Queue

def decreasing_edges(G,s,t):
    visited = [0 for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    cost_to = [0 for _ in range(len(G))]
    q = Queue()
    visited[s] = 1
    q.put((s,float('inf')))
    while not q.empty():
        v = q.get()
        for u in G[v[0]]:#jeśli z jakiegoś innego wierzchołka dojdziemy
    #do sąsiada i był już on odwiedzony z innego wcześniej,
    #ale koszt poprzedni był większy niż obecny (krawędzi wchodzącej
    #z innej strony) to pomijamy bo musimy mieć
    #jak największe wagi żeby móc dla innych wag na krawędziach
    #przejść po mniejszych, a jak zejdziemy do jakiejś małej
    #to się możemy zablokować
    #or v[1] <= u[1] czyli krawędź do v[0] ma mniejszy koszt niż ta
    #z v[0] do u[0] czyli szlibyśmy po rosnących a chcemy po malejących
    #więc nie chcemy wchodzić do linijek niżej i dodawać tych
    #wierzchołków do kolejki
            if (visited[u[0]] == 1 and cost_to[u[0]] >= u[1]) or v[1] <= u[1]: continue
            parent[u[0]] = v[0]
            visited[u[0]] = 1
            cost_to[u[0]] = u[1]
            q.put(u)

    path = [t]
    k = t
    while parent[k] != None:
        path.append(parent[k])
        k = parent[k] #czyli cofamy się po parentach

    if path[-1] != s: return False,None #tylko gdy parent[k] = None
    #od początku przed while, czyli nie dotarliśmy tam
    return True, path[::-1]

G=[[(1,3),(3,4)],[(4,5)],[(1,1),(3,7)],[],[(2,6)]]
print(decreasing_edges(G,4,1))
print(decreasing_edges(G,0,2))
print(decreasing_edges(G,1,3))
G=[[(1,3),(2,4)],[(4,1)],[(3,7),(5,3)],
[(4,6),(5,5)],[(5,4)],[(0,2),(1,4)]]
print(decreasing_edges(G,2,0))
print(decreasing_edges(G,0,3))
print(decreasing_edges(G,2,1))