# Autostrady
# budujemy między miastami autostrady
# wagi to odległości Euklidesowe
# w(A,B) = ceil(d(A,B))
# zbliżają się wybory chcemy żeby zbudować
# w jak najkrótszym czasie między rozpoczęciem
# a zakończeniem budowy ostatniej autostrady
# wszystkie budujemy naraz -> powinny mieć jak
# najbliższe sobie wagi

# for i in range(V): #Bruteforce
#   for j in range(V): #O(V^2)
#       if i != j:
#           E' = sorted(E, key = lambda e: abs(w(e) - w(i->j))) #O(V^2*logV)
#       tree = Kruskal(E', start = (i,j)) #O(V)
#       time = max_w(tree)-min_w(tree) #O(V)
# O(V^4*logV)

# szybciej, najpierw E' = sorted(E) , bez tego if i != j
# w Kruskalu potem [ , , , ,(i,j), , , ] i na lewo i prawo się
# rozchodzimy i wybieramy optymalniejsze do MST, O(V^4)


from math import inf
#O(V^4 * logV) :
class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value

def findset(x):
    if x.parent != x:
        x.parent = findset(x.parent)
    return x.parent

def union(x, y):
    x = findset(x)
    y = findset(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def kruskal(E, n):  # E już posortowane d[2] rosnąco
    A = []
    V = [Node(i) for i in range(n)]
    for e in E:  # lub while
        u, v, w = e
        if findset(V[u]) != findset(V[v]):
            union(V[u], V[v])
            A += [e]
    if len(A) < n - 1: return A, inf  # czyli niespójny
    return A, A[-1][2] - A[0][2]


def lowest_diff(E, n):
    m = len(E)
    E = sorted(E, key=lambda d: d[2])
    A, a = kruskal(E, n)
    mini = a #różnica między rozpoczęciem a zakończeniem
    #w minimalnym drzewie MST
    min_E = A
    if mini != inf:
        for i in range(1, m):
            A, a = kruskal(E[i:], n) #i pomijamy 'i' początkowych
#bo wtedy różnica między największą a najmniejszą się może potencjalnie
#zmniejszyć, szukamy MST na E[i:] = E[i],...E[n]
#nie patrzymy na podzbiory listy E bo na pewno będą miały <= różnicę
#jak tutaj E[i:], tzn np nie ma sensu od tyłu ograniczać listy E,
#bo jeśli np na zbiorze E[i:j] byłoby jakieś MST to jest to tym samym
#MST co na zbiorze E[i:], bo i tak największa waga będzie najmniejsza
#jaka tylko może być więc na różnicę nie wpłynie
            if a == inf: break #czyli niespójne drzewo
#szukamy żeby różnica była najmniejsza, więc może się właśnie
#opłacać brać duże wagi bo między nimi będzie mniejsza różnica :)...
            if mini > a:
                mini = a
                min_E = A
    if mini == inf: return "not coherent"
    return mini, min_E

#jeśli graf dany przez listę współrzędnych (x,y)
#to robimy listę list (sąsiedztwa) i dla każdej pary i!=j
#dodajemy raz append.u (v,w), raz append.v (u,w), gdzie w
#to w = (u,v) euklidesowa
E=[(0,1,12),(0,2,5),(1,0,12),(1,2,10),(2,0,5),(2,1,10),
(2,3,20),(2,4,14),(3,2,20),(3,4,12),(3,5,1),(4,2,14),
(4,3,12),(4,6,18),(5,3,1),(5,7,7),(5,8,6),(6,4,18),(6,7,9),
(7,5,7),(7,6,9),(7,9,8),(8,5,6),(8,9,19),(9,7,8),(9,8,19)]
print(lowest_diff(E,10))
E=[(0,1,12),(0,3,11),(1,0,12),(1,2,9),(1,6,17),(2,1,9),(2,3,7),
(2,7,14),(3,0,11),(3,2,7),(3,4,15),(4,3,15),(4,5,13),(4,7,10),
(5,4,13),(5,6,20),(6,1,17),(6,5,20),(6,7,11),(7,2,14),(7,4,10),(7,6,11)]
print(lowest_diff(E,8))