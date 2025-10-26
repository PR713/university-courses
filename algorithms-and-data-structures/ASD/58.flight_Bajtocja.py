#Najpierw szukam n, czyli liczby wierzchołków w grafie,
#ponieważ z założeń zadania u_i < v_i więc szukam n = max(v_i) + 1,
#dzięki temu tworzę listę visited i sąsiedztwa o długości 'n'.
#Funkcja DFSvisit przeszukuje w głąb sąsiadów wierzchołka rekurencyjnie
#i sprawdza możliwość przelotu z punktu startowego do docelowego,
#zapisując w prev_min i prev_max poprzednie wartości
#min i max_height, które są niezbędne przy kolejnych wywołaniach
#rekurencyjnych. Jeśli sąsiad wierzchołka nie został odwiedzony
#i abs(max(max_height, u[1]) - min(min_height, u[1])) <= 2*t,
#gdzie u[1] to optymalny pułap przelotu danym tunelem,
#a 2*t to maksymalna różnica między pułapami, to aktualizujemy
#min i max_height i sprawdzamy czy gdzieś funkcja zwróci nam True.
#W wywołaniu rekurencyjnym jeśli odwiedzimy wszystkich sąsiadów już to
#ustawiamy go znowu na nieodwiedzonego, żeby być może tunelem z innego
#wierzchołka go znowu odwiedzić i zwracamy w tym wywołaniu False.
#Jeśli dotrzemy do wierzchołka 'y' to zwracamy True,
#jeśli nigdy nie dotrzemy to False.
#Złożoność czasowa to O(n!), n - liczba wierzchołków

#wcześniej z flagą nonlocal to jak się wszystkie wywołania
#zakończą to dopiero zwraca czy gdzieś było jakieś True
#a tu szybciej, pierwsze możliwe

def Flight(L, x, y, t):
    n = max(v for _, v, _ in L) + 1  # liczba wierzchołków w grafie
    visited = [False] * n
    l_sasiedztwa = [[] for _ in range(n)]
    for u, v, p in L:
        l_sasiedztwa[u].append((v, p))
        l_sasiedztwa[v].append((u, p))  # nieskierowany

    min_height = None
    max_height = None

    def DFSvisit(source, min_height, max_height):
        prev_min = min_height
        prev_max = max_height
        # ^zachowują wysokości z jakimi były wywołane kolejne
        # wywołania rekurencyjne, jeszcze przed zaktualizowaniem
        # w for na wartość = min( , ) i max( , ) :)
        visited[source] = True
        if source == y:  # warunek końca
            return True
        for u in l_sasiedztwa[source]:
            if source == x:  # gdy jesteśmy w 'x' i patrzymy na sąsiadów
                # tyle razy się wykona ile jest
                # tunelów zawierających wierzchołek 'x'
                min_height = u[1]
                max_height = u[1]
            if not visited[u[0]] and abs(max(max_height, u[1]) - min(min_height, u[1])) <= 2 * t:
                min_height = min(min_height, u[1])
                max_height = max(max_height, u[1])
                if DFSvisit(u[0], min_height, max_height):
                    return True
                min_height = prev_min
                max_height = prev_max
        visited[source] = False
        return False

    return DFSvisit(x, min_height, max_height)
