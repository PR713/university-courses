
#Radosław Szepielak
#Tworzę listy dwuwymiarowe visited oraz distance, w jednym wierszu
#przechowujące wartości dla normalnego przejścia, a w drugim dla
#przejścia z butami milowymi. Za każdym razem w pętli while True
#szukamy wierzchołka który nie został jeszcze odwiedzony przez któryś
#rodzaj przejścia krawędzi i którego odległość od wierzchołka startowego
#'s' jest najmniejsza, a następnie ustawiamy go na odwiedzonego przez
#dany sposób przejścia. Jest to podobne do algorytmu Dijkstry. Szukamy
#wierzchołka którego odległość od 's' jest najmniejsza po to, żeby to
#z niego próbować iść dalej normalnie lub butami dwumilowymi - jest on
#optymalnym kandydatem do najkrótszej ścieżki z 's' do 'w'. Następnie
#dla danego sposobu przejścia odpowiednio wykonuję relaksację krawędzi.
#Dla butów dwumilowych sprawdzam czy można z wierzchołka v[1] przejść
#skokiem przez 'k' do 't' i wykonuję relaksację.
#Złożoność czasowa O(V^3), bo O(V*(V + V + V^2))
#Złożoność pamięciowa O(V)
#Z kolejką byłoby O(V*(logV + V*logV + V^2*logV) = O(V^3 * logV)
#Z kopcem Fibonacciego już O(V*(logV+ V + V^2) = O(V^3)
#byłoby ciut lepsze w składowych złożonościach.

#Dijkstra sama w sobie macierzowo ma O(V^2 * logV) - z kolejką na binarnym,
#a bez niej/Fibonaccim ma O(V*(V+V)) = O(V^2) lub zamienić na listę sąsiedztwa
#O(V^2 + ElogV) zrobić, w najgorszym przypadku mamy tą gorszą macierzową
#O(V^2 logV) dla pełnego

#więc tu listowo O(V^2 + V*(logV + e*logV + e*e*logV) =
#= O(V^2 + VlogV + ElogV + eElogV) = O(V^2 + eElogV) - gorzej dla pełnego V^3 logV
#więc na kopcu Fibonacciego mamy O(V^2 + VlogV + E + eE) = O(V^2 + eE)
#co jest <= od O(V^3) :)
#bez Fibonacciego V^2 + VE można robiąc do skoków dwumilowych
#nowy graf najpierw 3 fory

def the_next_vertex(distance,visited):
    #wybieramy taki wierzchołek który był uprzednio zrelaksowany
    #i jest jeszcze nieodwiedzony do którego ścieżka dowolnym
    #sposobem przejścia jest najkrótsza od źródłowego 's'
    v = None
    value = float('inf')
    n = len(distance[0])
    for i in range(2):
        for u in range(n):
            if visited[i][u] == 0 and distance[i][u] < value:
                value = distance[i][u]
                v = (i,u) #i - rodzaj poruszania, u wierzchołek

    if v: visited[v[0]][v[1]] = 1
    return v

def jumper(G, s, w):
    n = len(G)
    visited = [[0 for _ in range(n)] for _ in range(2)]
    distance = [[float('inf') for _ in range(n)] for _ in range(2)]
    distance[0][s] = 0 #żeby można było najpierw wykonać dowolny ruch

    while True:
        v = the_next_vertex(distance, visited) #krotka
        if v == None:
            return float('inf') #oznacza że 'w' nie jest osiągalny z 's'

        if v[1] == w:
            return distance[v[0]][v[1]]

        for u in range(n): #zwykłe przejście
            if G[v[1]][u] > 0:# and visited[0][u] == 0: #i dotąd nieodwiedzony
            # nie trzeba visited[0][u] i niżej [1][t] bo jeśli jest już odwiedzony
            # to i tak if niżej z relax nie puści go :) aczkolwiek czasami sprawdzenie
            #tego może być szybsze niż liczenie potem maksa itp niżej :D
                if distance[0][u] > distance[v[0]][v[1]] + G[v[1]][u]:
                    distance[0][u] = distance[v[0]][v[1]] + G[v[1]][u]

        if v[0] == 0: #czyli przyszliśmy normalnie
            for k in range(n): #chcemy iść butami dwumilowymi
                for t in range(n):
                    if G[v[1]][k] > 0 and G[k][t] > 0 and v[1] != t:# and visited[1][t] == 0:
                        if distance[1][t] > distance[v[0]][v[1]] + max(G[v[1]][k], G[k][t]):
                            distance[1][t] = distance[v[0]][v[1]] + max(G[v[1]][k], G[k][t])

S=[[0, 1, 0, 0],
   [1, 0, 4, 0],
   [0, 4, 0, 3],
   [0, 0, 3, 0]]
s=0
w=3
print(jumper(S,s,w))




