
#Psucie ścieżki, dany G(V,E) nieskierowany i s,t należy do V,
#Czy istnieje e należące do E takie, że po jej
#usunięciu ścieżka s -> t się wydłuży (lub przestanie ona istnieć!!!)
#Policzyć ile wierzchołków leży w odległości k
#od początku i końca ścieżki (?)
#bo trudne jest napisanie BFS który wykryje niezależne ścieżki
#ale łatwo znaleźć informację o tym ile
#wierzchołków leży w odległości x od początku 's' ścieżki
#jeśli np długość najkrótszej ścieżki do 't' to 7
#to szukamy wszystkich wierzchołków które są w odległości
#6 od 's' bo mogą leżeć na innej najkrótszej ścieżce
from queue import Queue

def BFS(G,s):
    Q = Queue()
    n = len(G)
    distance = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    Q.put(s)
    while not Q.empty():
        v = Q.get()
        for u in G[v]:
            if not visited[u]:
                distance[u] = distance[v] + 1
                Q.put(u)
                visited[u] = True #albo trzeba by było
            #sprawdzać visited zaraz po każdym zdjęciu z kolejki
    return distance

def krawedz(G,s,t):
    distance_1 = BFS(G,s)
    distance_2 = BFS(G,t)
    min_len_path = distance_1[t]
    cnt = [0 for _ in range(min_len_path + 1)]

    #zliczamy ile jest wierzchołków w odległości
    #równej min_len_path
    for v in range(len(G)):
        if distance_1[v] + distance_2[v] == min_len_path:
            cnt[distance_1[v]] += 1

    for i in range(min_len_path):#cnt[i] to ilość wierzchołków
        #na ścieżce długości 'i' ( w odległości 'i' od 's'
        #można też cnt[distance_2[v]] i wtedy od 't' ale symetryczne)
        if cnt[i] == cnt[i+1] == 1:
        #^czyli są połączone tylko jedną krawędzią
        #która można usunąć i zniszczymy najkrótszą ścieżkę
        #i być może się wydłuży a może przestanie istnieć :)
        #    _   _
        # s_/ \_/ \_ t
        #   \_/ \_/ np te w odległości 4 i 5
            return True
    return False