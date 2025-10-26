
#Przewodnik turystyczny
#Chcemy przewieźć turystów z A do B ale na danym
#odcinku można transportować tylko określoną liczbę
#osób, na ile najmniej trzeba podzielić grupę ludzi,
#żeby ich dowieźć do B

#sortujemy wagi krawędzi malejąco
#sort(edges, reverse = True) #ElogE

#g = empty_graph() #pusty graf jako macierz VxV
#for e in edges:
#   graph.add(e) #i jej wagę
#   dfs/bfs(G,a,b)
#   if ok: return e.weight ## złożoność O(E*V^2)

#lub find union zbiory rozłączne i łączymy parami (?)

#***lub kolejka, bez visited, wpisujemy wagi w wierzchołkach
#jako informację ile osób można do nich najwięcej
#przewieźć jakąś ścieżką

from queue import Queue
from math import ceil
#pomysł ***
def Transport(G,s,k,n):
    q=Queue()
    m=len(G)
    weights=[0 for _ in range(m)]
    parent=[None for _ in range(m)]
    q.put(s)
    weights[s]=n #w pierwszym liczba osób
    while not q.empty():
        v=q.get()
        for u in G[v]:
            w=min(u[1],weights[v]) #min z aktualnej wagi do którego
        #sprawdzamy i wagi obecnej maksymalnej w którym jesteśmy (v)
            if w>weights[u[0]]:#aktualizujemy maks liczbę osób
                #jaką można w ten sposób dowieźć
                #początkowo weight to lista zer
                parent[u[0]]=v
                weights[u[0]]=w
                q.put(u[0])
    path=[]
    t=k
    while t!=None:
        path.append(t)
        t=parent[t]
    path.reverse()
    return path,weights[k],ceil(n/weights[k])

#testy
G=[[(1,25),(2,50)],[(0,25),(2,10),(3,50)],[(0,50),(1,10),(3,20)],
[(1,50),(2,20),(4,9),(5,7),(6,15)],[(3,9),(5,11),(6,14)],
[(3,7),(4,11),(6,10)],[(3,15),(4,14),(5,10)]]
print(Transport(G,0,5,100))
G=[[(1,17),(2,31),(3,11)],[(0,17),(2,19),(3,25)],[(0,31),(1,19),(4,15)],
[(0,11),(1,25),(4,13),(5,7)],[(2,15),(3,13),(5,14)],[(3,7),(4,14)]]
print(Transport(G,0,5,300))
G=[[(1,12),(2,12),(3,10)],[(0,12),(2,8),(4,15)],[(0,12),(1,8),(3,4),(4,7)],
[(0,10),(2,4),(4,11)],[(1,15),(2,7),(3,11)]]
print(Transport(G,3,2,50))