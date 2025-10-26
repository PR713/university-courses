#naukowiec A do laboratorium B
#a naukowiec B do laboratorium A
#i nie mogę się zbliżyć na odległość 'd'
#czyli najkrótsza ścieżka między nimi > d
#przechodzą po jednej krawędzi w danym momencie
#wszystkie wagi to 1 #zrobione ciężej bo różne wagi
#czy istnieje takie przejście żeby nie wybuchli
#G = graf pełny bez (a,b), (b,a)

#tworzymy graf stanów i przejść
#zapisujemy w grafie wszystkie możliwe przejścia
#iterujemy przez wszystkie pary wierzchołków/krawędzie
#i Floyd Warshall odległość najmniejsza między każdą parą
#potem O(n^2) przejść mamy
#i jeśli kolejno między którymiś istnieje ścieżka o wadze > d
#to je łączymy... dostajemy finalnie ścieżkę jak mają iść :)


from queue import Queue
from math import inf

#pomocnicze funkcje
def Floyd_Warshall(G): #G macierzowo, nieskierowany
    n = len(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if G[i][j] > G[i][k] + G[k][j]:
                    G[i][j] = G[i][k] + G[k][j]
    return G

def BFS(G,s):
    n = len(G)
    Q = Queue()
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                visited[v] = True
                parent[v] = u
                Q.put(v)
    return d, parent, visited

def nuclear_transport(G,s,t,d):
    n=len(G)
    Gr = [[G[i][j] for j in range(n)] for i in range(n)] #Gr kopia G
    G = Floyd_Warshall(G) #G to najkrótsze ścieżki między parą, P poprzednicy
    new_G = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] != inf and G[i][j] > d:
                new_G[i][j] = True #między jakimi parami > d
    if not G[s][t]: return False
    Graph = [[] for _ in range(n * n)]
    #W tym przypadku, n*s + t reprezentuje stan, w którym naukowiec
    #A jest w laboratorium s, a naukowiec B jest w laboratorium t.
    for i in range(n):
        for j in range(n):
            if new_G[i][j]: #jeśli > d
                for k in range(n):#i -...- j -- k
                    #               \........../
                    #Osoba A, (i,j) i (i,k) > d
                    if k != j and new_G[i][k] and Gr[j][k] != inf:
                        Graph[n * i + j].append(n * i + k)
#TO że w 'i' zostaje A, natomiast B idzie z 'j' do 'k',
#jedną krawędź przechodzi
                #                   /-----------\
                for k in range(n):# i -...- j     k
                    #                        \.../
                    #Osoba B, (k,j) i (i,j) > d
                    if k != i and new_G[k][j] and Gr[i][k] != inf:
                        Graph[n * i + j].append(n * k + j)
#TO że w 'j' zostaje B, natomiast A idzie z 'i' do 'k'
#więc potem Graph[n*i+j] ma odnośnik do wierzchołka n*k+j
#czyli dokąd może się przemieścić
    d, par, vis = BFS(Graph, n * s + t) #Osoba A w s, Osoba B w t
    k = n * t + s
    path = []
    while k != None:
        path.append((k // n, k % n)) #cofamy się skąd przyszliśmy
        k = par[k]
    path.reverse()
    if path[0] != (s, t): return False
    return True, path

#któryś naukowiec może zostać w wierzchołku podczas gdy drugi się rusza
##Dodatkowo, jeśli obaj naukowcy muszą się poruszać jednocześnie:
#to tylko to, a jeśli mogą to dodatkowo dopisujemy to
#                for k in range(n):# i -...- j     k
#                    #                        \.../
#                    #Osoba A, (i,j) i (k,j) > d
#                    if k != i and new_G[k][j] and Gr[i][k] != inf:
#                        for l in range(n):# j -...- k     l
#                            #                        \.../
#                            #Osoba B, (j,k) i (j,l) > d
#                            if l != j and new_G[j][l] and Gr[k][l] != inf:
#                                Graph[n * i + j].append(n * k + l)


G=[[0,7,5,inf,inf,inf],
   [7,0,8,3,6,inf],
   [5,8,0,inf,10,inf],
[inf,3,inf,0,inf,12],
   [inf,6,10,inf,0,7],
   [inf,inf,inf,12,7,0]]
print(nuclear_transport(G,0,5,7))
G=[[0,8,8,inf],[8,0,2,6],[8,2,0,5],[inf,6,5,0]]
print(nuclear_transport(G,0,3,3))
G=[[0,7,inf,inf,11],[7,0,4,10,inf],[inf,4,0,6,5],[inf,10,6,0,10],[11,inf,5,10,0]]
print(nuclear_transport(G,0,3,5))
G=[[0,7,5,inf,inf,inf,inf],[7,0,4,inf,inf,inf,inf],[5,4,0,inf,inf,inf,inf],
[inf,inf,inf,0,10,6,7],[inf,inf,inf,10,0,12,inf],
[inf,inf,inf,6,12,0,9],[inf,inf,inf,7,inf,9,0]]
print(nuclear_transport(G,0,4,1))