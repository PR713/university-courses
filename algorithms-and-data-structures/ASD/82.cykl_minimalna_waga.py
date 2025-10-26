
#znaleźć cykl o minimalnej wadze, G skierowany
#dodatnie wagi

def Floyd_Warshall(G):
    n = len(G)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if G[j][k] > G[j][i] + G[i][k]: # S = min( , )
                    G[j][k] = G[j][i] + G[i][k]

def find_cycle(G):
    n = len(G)
    for i in range(n):
        G[i][i] = float('inf') #sam do siebie nie, G skierowany
    Floyd_Warshall(G)
    min_dis = float('inf')
    for i in range(n):
        min_dis = min(G[i][i], min_dis) #G[i][i] długość cyklu
    if min_dis != float('inf'): return min_dis
    return float('inf')