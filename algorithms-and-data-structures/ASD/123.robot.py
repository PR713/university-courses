from heapq import heappop, heappush

COST = [60, 40, 30]

def robot(L, A, B):
    n = len(L)
    m = len(L[0])

    # graph[i][j][s][l] - i-ty wiersz, j-ta kolumna, s-ty kierunek, l-ta warstwa
    graph = [[[[[] for _ in range(3)] for _ in range(4)] for _ in range(m)] for _ in range(n)]

    # obroty
    for i in range(n):
        for j in range(m):
            for s in range(4):
                for l in range(3):
                    graph[i][j][s][l].append(((i, j, (s + 1) % 4, 0), 45))
                    graph[i][j][s][l].append(((i, j, (s - 1) % 4, 0), 45))

    # przesunięcia do przodu
    for i in range(n):
        for j in range(m):
            for l in range(3):
                if i + 1 < n and L[i + 1][j] != 'X':
                    graph[i][j][0][l].append(((i + 1, j, 0, min(2, l + 1)), COST[l]))
                if j + 1 < m and L[i][j + 1] != 'X':
                    graph[i][j][1][l].append(((i, j + 1, 1, min(2, l + 1)), COST[l]))
                if i - 1 >= 0 and L[i - 1][j] != 'X':
                    graph[i][j][2][l].append(((i - 1, j, 2, min(2, l + 1)), COST[l]))
                if j - 1 >= 0 and L[i][j - 1] != 'X':
                    graph[i][j][3][l].append(((i, j - 1, 3, min(2, l + 1)), COST[l]))

    # Dijkstra
    start = (0, (A[1], A[0], 1, 0))
    dist = [[[[float('inf') for _ in range(3)] for _ in range(4)] for _ in range(m)] for _ in range(n)]

    queue = [start]
    while queue:
        d, (i, j, s, l) = heappop(queue)
        if dist[i][j][s][l] <= d:
            continue
        dist[i][j][s][l] = d #git bo wczesniej nie aktualizujemy dist :)
        for (ni, nj, ns, nl), c in graph[i][j][s][l]:
            if d + c < dist[ni][nj][ns][nl]:
                heappush(queue, (d + c, (ni, nj, ns, nl)))

    result = min(dist[B[1]][B[0]][s][l] for s in range(4) for l in range(3))
    if result == float('inf'):
        return None
    return result
