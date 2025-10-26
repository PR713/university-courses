def visit(graph, node, visited, parents, height):
    curr_height = height
    max_height = curr_height
    global time
    time +=1   #wierzchołek został odwiedzony i time to czas odwiedzenia
    visited[node] = True
    for neighbour in graph[node]:
        if visited[neighbour] == False:
            parents[neighbour] = node
            curr_height = visit(graph, neighbour, visited, parents, height + 1)
            if max_height < curr_height:
                max_height = curr_height
    time +=1
    return max_height

def DFS(graph, start):
    n = len(graph)
    z = float('inf')
    parents = [None for i in range(n)]
    visited = [False for i in range(n)]
    global time
    time = 0
    z = visit(graph, start, visited, parents, 0)
    return z

def best_root( L ):
    n = len(L)
    min_node = None
    min_height = float('inf')
    for i in range(n):
        a = DFS(L, i)
        if a < min_height:
            min_height = a
            min_node = i

    return min_node