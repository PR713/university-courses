#Cykl Eulera
def EulerCycle(G,start_v): #od dowolnego zaczynamy
    def DFSvisit(G,u):
        for i in range(len(G)):
            if G[u][i]: #jeśli jest krawędź
                M[u][i] = 0
                M[i][u] = 0 #graf nieskierowany
                DFSvisit(G,i)
        cycle.append(u) #dodajemy po przetworzeniu w postaci odwiedzenia
        #wszystkich wychodzących krawędzi, bo do wierzchołka możemy
        #wchodzić wiele razy dopóki wszystkich krawędzi nie odwiedzimy
        #gdy już odwiedzimy wszystkie krawędzie z danego wierzchołka
        #pierwszy przetworzony to będzie ten z którego startujemy, bo musimy
        #w końcu do niego wrócić i potem kolejne dodajemy, można dostać różne
        #cykle Eulera, zależy jak DFS przemierzy graf, ogólnie nigdy się nie
        #zablokujemy i zawsze najpierw wrócimy do start_v, potem jakiś poprzedni itd
    #jak się cofjniemy od start_v to tamten poprzedni ma st. parzysty i wszystkie
    #inne też, więc znowu do niego znów musimy wrócić i potem od niego się cofać, czyli będziemy
    #doklejać cykle wewnątrz cyklu, start_v ... b c d a b start_v
    n = len(G)
    for i in range(n):
        if len(G[i]) == 0 or len(G[i]) % 2 == 1: return False

    M = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            M[i][j] = 1

    cycle = []
    DFSvisit(M,start_v)
    return True, cycle

G=[[1,6],[0,2],[1,3,6],[2,4,5],[3,5],[3,4],[0,2,7],[6]]
print(EulerCycle(G,1))
G=[[1,3],[0,2],[1,3],[0,2]]
print(EulerCycle(G,3))
G=[[1,2],[0,2,3,4,5,6],[0,1,3,4,5,6],[1,2,4,5],[1,2,3,5],[1,2,3,4],[1,2]]
print(EulerCycle(G,0))
G=[[1,8],[0,2],[1,3],[2,4],[3,5,7],[4,6],[5,7],[4,6,8],[7,0]]
print(EulerCycle(G,8))