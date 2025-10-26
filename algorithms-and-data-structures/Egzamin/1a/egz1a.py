#Radosław Szepielak
#Najpierw zamieniam reprezentację grafu z listy krawędzi na listę sąsiedztwa.
#Następnie tworzę nową listę new_B bazującą na liście B, tak żeby na danym
#indeksie 'i' przechowywała informację o tym, jaki jest najniższy możliwy iloraz
#p/q spośród wszystkich znajdujących się w danym wierzchoku 'i', ponieważ wyższe
#ilorazy dałyby tylko i wyłącznie gorsze czasy w Duathlonie. Jeśli w danym
#wierzchołku nie ma roweru to wartość p/q to float('inf'). Następnie używam
#standardowego algorytmu Dijkstry, raz z wierzchołka 's' i dostaję tablicę d1
#dystansów z 's' do reszty wierzchołków, drugi raz z wierzchołka 't', dostaję
#tablicę d2. Dzięki temu mogę potem łatwo obliczyć minimalny czas Luizy,
#ponieważ rozważam po kolei wszystkie wierzchołki 'i' i dla każdego robię minimum
#z dotarcia biegnąc od 's' do 'i' czyli d1[i] oraz + d2[i] * (p/q) co oznacza jazdę
#najlepszym rowerem z 'i' do 't'. Następnie rozważam już samo normalne biegnięcie
#z 's' do 't' bez używania roweru (d1[t]) i liczę z tego finalnie minimum. Wynikiem jest
#dist_mini zaokrąglone w dół czyli floor(dist_mini).
#Złożoność czasowa O(ElogV)
#Złożoność pamięciowa O(E+V)

from egz1atesty import runtests
from queue import PriorityQueue
from math import floor

def edges_to_adj(E):
    n = 0
    for u, v, _ in E: #O(E)
        n = max(n, max(u, v))
    n = n + 1 #wierzchołki numery od 0,...,n-1
    adj_list = [[] for _ in range(n)]
    for u, v, w in E:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    return adj_list


def Dijkstra(B, G, s):
    n = len(G)
    Q = PriorityQueue()
    d = [float('inf') for _ in range(n)]
    Q.put((0,s))
    d[s] = 0
    while not Q.empty():
        w, u = Q.get()
        if w == d[u]:
            for v,c in G[u]:
                if d[v] > d[u] + c:
                    d[v] = d[u] + c
                    Q.put((d[v], v))
    return d


def edit_B(B,n1): #najniższe p/q
    new_B = [[None, float('inf'), 1] for _ in range(n1)]
    for b in B: #O(V)
        p1 = new_B[b[0]][1]
        q1 = new_B[b[0]][2]
        p = b[1]
        q = b[2]
        if p1/q1 > p/q:
            new_B[b[0]] = [b[0], p, q]

    return new_B

def armstrong(B, G, s, t):
    new_G = edges_to_adj(G)
    n1 = len(new_G)
    new_B = edit_B(B,n1)
    d1 = Dijkstra(new_B,new_G,s) # z s do i
    d2 = Dijkstra(new_B,new_G,t) #z t do i
    dist_mini = float('inf')

    for i in range(n1):
        p, q = new_B[i][1], new_B[i][2]
        dist_mini = min(dist_mini, d1[i] + d2[i] *(p/q))

    dist_mini = min(dist_mini, d1[t]) #po prostu tylko biegnąc z 's' do 't'

    return floor(dist_mini)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(armstrong, all_tests=True)
