
#Graf gdzie każda krawędź ma odległość
#w kilometrach między miastami, a na wierzchołkach
#cenę za litr paliwa
#palimy 1l / 1km
#bak ma jakąś pojemność D w litrach
#dla każdej krawędzi e: D > e,
#znajdujemy najtańszą trasę
from queue import PriorityQueue
from math import inf

def cheapest2(G,start,end,D):
    n=len(G)
    Graph=[[inf for _ in range(D+1)] for _ in range(n)]
    d=[inf for _ in range(n)]
    q=PriorityQueue()
    q.put((0,0,start))
    while not q.empty():
        c,f,v = q.get()
        if d[v]>c: #jeśli znajdujemy mniejszy koszt to aktualizujemy
            d[v]=c
        for i in range(D+1-f): #i to ilość jaką można zatankować
            #żeby mieć już cały zalany bak D
            if c+i*G[v][1]<Graph[v][i+f]: #jeśli c - koszt dotarcia do v,
            #+ ilość zatankowanego * cena jest mniejsza od dotychczasowych
            #dotarć do tego [v] w Graph z ilością paliwa i+f,
            #które sprawdzamy dla wszystkich 'i' w forze, (tankujemy
            #różne wartości albo tylko ciut, albo aż na maxa bak)
            #to akualizujemy minimum na podstawie którego potem będziemy
            #bazować znowu
            #może jednak nam braknąć paliwa, to są realia a nie
            #idealne warunki *** niżej, więc znajdziemy koszt <=
            #niż w idealnych, bo może np na styk wystarczyć :)
                Graph[v][i+f]=c+i*G[v][1]
                for u,e in G[v][0]: #e to długość drogi, palimy 1l/1km
                #więc też ilość paliwa potrzebna do przejechania odcinka
                #więc jeśli mamy ilość paliwa i + f co najmniej pozwalającą
                #na przejechanie to jedziemy .put :)
                    if i+f>=e: #***
                        q.put((c+i*G[v][1],i+f-e,u))
    return d[end]


G=[[[(1,42),(4,35)],5.70],[[(0,42),(2,25),(4,15)],6.20],
[[(1,25),(3,31),(5,65)],6.05],[[(2,31),(5,42)],5.10],
[[(0,35),(1,15),(5,52)],5.30],[[(2,65),(3,42),(4,52)],4.90]]
print(cheapest2(G,0,3,50))