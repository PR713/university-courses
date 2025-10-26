
#uruchamiamy DFS
#po przetworzeniu wierzchołka dopisujemy go na początek listy
#bo pierwszy wierzchołek zostanie przetworzony na końcu :)
#to jest dokładnie sortowanie topologiczne DAG'u i to
#daje ścieżkę Hamiltona

def Hamilton(G):
    visited = [0]*len(G)
    A = []
    def visit(G,v,A):
        nonlocal visited #listy są modyfikowalne
        #tylko zmienne trzeba nonlocal
        visited[v] = 1
        for u in G[v]:
            if not visited[u]:
                visit(G,u,A)
        A.append(v)

    for i in range(0,len(G)):
        if not visited[i]:
            visit(G,i,A)
    A.reverse() #trzeba odwrócić
    for i in range(0,len(G)-1):#ścieżka ma długość n-1
        u = A[i]
        v = A[i+1]#i sprawdzamy czy każde kolejne dwa są połączone
        if v not in G[u]:#lub na odwrót ale chyba OK
            return False
    return True

G=[[1],[2],[0,3],[4],[5],[3]]
print(Hamilton(G))
G=[[1],[2],[3],[1],[3,5],[3]]
print(Hamilton(G))