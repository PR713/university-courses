#G nieskierowany, dany macierzowo. Proszę podać algorytm
#sprawdzający czy graf ma cykl dł. 4
#lepiej niż O(V^4)
#próbujemy dla każdej pary wierzchołków
#znaleźć trzeci wierzchołek połączony
#patrząc na ich wiersze i czy dla jakiejś kolumny
#oba mają '1' i jeśli znajdziemy takie dwa wierzchołki
#w różnych kolumnach i przerywamy to mamy 4 wierzchołki
#bo jak będzie więcej to i tak cykl długości 4
#O(V^3)
# -----v-----
# ?----|----?
# -----u-----

def cycle_4(G):
    n = len(G)
    for i in range(n):
        for j in range(i+1,n):
            cnt = 2
            for k in range(n):#wiersze
                if G[i][k] == 1 and G[j][k] == 1:
                    cnt += 1
                if cnt == 4: return True
    return False

G = [[0,1,0,0,1],
     [1,0,0,1,0],
     [0,0,0,0,1],
     [0,1,0,0,1],
     [1,0,1,1,0]]
print(cycle_4(G))