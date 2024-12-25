
#alg. Dijkstra reprezentacja macierzowa
from queue import PriorityQueue
#O(V*(logV + V*logV) = O(V^2* logV) ~ ElogV
#więc albo najpierw na listę sąsiedztwa O(V^2) i normalnie ElogV
#lub bez kolejki tylko jak w 86. i wyjdzie O(V^2)
def dijkstra(graph,start):#,end):
    distances = [float('inf') for _ in range(len(graph))]
    distances[start] = 0
    Q = PriorityQueue()
    Q.put((0,start))
    while not Q.empty():
        w,current = Q.get()
        for i in range(len(graph)):
            if graph[current][i] != 0: #czy jest krawędź
                new_distance = graph[current][i] + w
                if new_distance < distances[i]:
                    #ewentualnie parent[i] = current
                    distances[i] = new_distance
                    Q.put((new_distance,i))
    return distances

###################################


def next(distances, visited):
    v = None
    n = len(distances)
    value = float('inf')
    for i in range(n):
        if not visited[i] and distances[i] < value:
            value = distances[i]
            v = i

    if v != None: visited[v] = True
    return v

def Dijkstra(G: 'represented by matrix',start):
    n = len(G)
    distances = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    distances[start] = 0
    while True:
        next_v = next(distances,visited)
        if next_v is None: break
        #if next_v == e: return distances
        for u in range(n):
            if G[next_v][u] > 0 and not visited[u]: #też nie trzeba not visited
            #jeśli byłby odwiedzony to niżej if relax nie wpuści już z mniejszą
                if distances[u] > distances[next_v] + G[next_v][u]:
                    distances[u] = distances[next_v] + G[next_v][u]
    return distances

S=[[1, 1, 3, 0],
   [1, 0, 4, 0],
   [0, 4, 2, 3],
   [0, 0, 7, 0]]
print(dijkstra(S,0))
print(Dijkstra(S,0))