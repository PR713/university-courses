
#Graf ważony, wagi {1,...,|E|}
#parami różne. Znaleźć ścieżkę s -> t
#o minimalnej sumie wag i malejących wagach

from heapq import heappush, heappop
def czwarte(G,start,end):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    Q = []
    heappush(Q,(0,start,float('inf')))
    #trzeci element krotki dodatkowo trzeba mieć
    #krawędź jaką dotarliśmy, żeby wiedzieć czy malejące
    #modyfikacja Dijkstry
    distance[start] = 0
    while len(Q) > 0:
        x,v,prev = heappop(Q)
        for w,u in G[v]:
            if distance[u] > distance[v] + w and w < prev:
                distance[u] = distance[v] + w
                heappush(Q,(distance[u],u,w))
    return distance

#lub posortować krawędzie po wadze ElogE...

#piętra zrobić i krawędzie zstępujące na
#poziomy niżej, każdy wierzchołek ma E kopii