#G skierowany lista sąsiedztwa
#dobry początek czy istnieje wierzchołek z którego
#istnieje ścieżka do każdego wierzchołka

def poczatek(G):
    def DFSvisit(i):
        nonlocal G,times,time,visited
        #G, times i visited nie musi być nonlocal bo tablice i tak
        #są widoczne i modyfikowalne
        visited[i] = True
        #time += 1
        #times[i] = time to byłby czas wejścia (odwiedzenia)
        #np przy operatorze linii telefonicznych
        #likwidujemy od ostatniego czasu najwyższego
        for v in G[i]:#v sąsiedzi i
            if not visited[v]:
                DFSvisit(v)
        time += 1 #wyjścia już po całej pętli
        #gdy się cofamy rekurencją (przetworzenia)
        times[i] = time
        #na wykładzie time i przed i po for bo jak w Cormenie
        #po prostu zachowuje dosłownie czas
    #czas wyjścia bo gdyby to był czas przetworzenia
    #to od którego zaczynamy zawsze miałby czas równy 0
    #i nic nam to nie mówi o liczbie odwiedzonych
    #a czas wyjścia może być równy n dla pierwszego
    #do którego weszliśmy lub dla jakiegoś innego do
    #którego nie daliśmy rady wejść bo miał tylko skierowaną np

    n = len(G)
    times = [-1 for _ in range(n)]
    time = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:#w nieskierowanym niespójności
        #ale w skierowanym po prostu czasami możemy nie odwiedzieć
        #bo nie ma krawędzi wchodzącej z danego wierzchołka w dalszą
        #część grafu
    #z dowolnego robimy DFSvisit bo jeśli z niego nie odwiedzimy
    #jeszcze wszystkich to po prostu możliwe że istnieje lepszy
    #np położony za nim albo do którego nie da się dojść
    #czyli niespójny
            DFSvisit(i)

    for i in range(n):
        if times[i] == n:#szukamy takiego który ma czas wyjścia równy len(G)
            s = i
            visited = [False for _ in range(n)]
            DFSvisit(s)#sprawdzamy potencjalnego kandydata
            #lub time = 0
            #return time == n
            return False in visited
    return False

