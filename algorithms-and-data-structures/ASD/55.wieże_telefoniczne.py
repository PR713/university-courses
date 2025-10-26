#Likwidujemy wieże telefoniczne
#mamy tak usuwać, żeby nie rozspójnić grafu
#używamy DFS i jak skończy się wywołanie
#wtedy te ostatnie wierzchołki do których doszliśmy
#usuwamy je - które przetworzyliśmy czasem time od tyłu

#dla BFS też można
#ogólnie powstaje nam jakieś drzewo i usuwamy
#po prostu liście,appendujemy na koniec listy wierzchołki
#które odwiedzamy po kolei i potem je pobieramy

from queue import Queue

def BFS(G,s):
    q = Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)] #odległości
    d[s] = 0
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                q.put(v)

    que = [(d[i], i) for i in range(n)]
    que.sort() #sortujemy po odległościach, key = lambda d[1]
    que = [que[i][1] for i in range(n)] #tylko same numery wierzchołków
    return que[::-1]

#lub DFS czas przetworzenia albo też kolejka po przetworzeniu
#czyli po zakończeniu fora w jakimś wywołaniu rekurencji

def DFS(G):
    def DFSvisit(G,s):
        nonlocal visited, que
        visited[s] = True
        for v in G[s]: #sąsiedzi s
            if not visited[v]:
                visited[v] = True
                DFSvisit(G,v)
        que.append(s)

    n = len(G)
    visited = [False for _ in range(n)]
    que = []
    for i in range(n):
        if not visited[i]:
            DFSvisit(G,i)
    return que


G = [[2,3],[3,4],[0],[0,1],[1]]
print(BFS(G,0)) #usuwanie odwrotnie niż idzie fala
print(DFS(G)) #usuwanie po przetworzeniu
# 2 - 0 - 3 - 1 - 4 numery wierzchołków i połączenie


