
#Domknięcie przechodnie, G skierowany,
#nieważony (reprezentacja?)
#Wyznaczyć G' taki że jeśli w G istnieje
#ścieżka to w G' istnieje krawędź między (u,v)
#nieważony ale jeśli w G ścieżka o wadze w
#to w G' krawędź o wadze w, wszystkie = 1

#Floyd Warshall
#copy tylko kopiuje raz
#deepcopy rekurencyjnie np listę list

def domkniecie(G):
    n = len(G)
    A = [[G[i][j] for i in range(n)] for j in range(n)]
    #G macierzowo True/False krawędzie

    for x in range(n):
        for y in range(n):
            for z in range(n):
                A[y][z] = (A[y][z] or (A[y][x] and A[x][z]))
                #przypisujemy jedno z dwóch albo jeśli istnieje już
    #ścieżka dł 1 bezpośrednio albo ścieżka dł 2
    return A
