#Radosław Szepielak
#W celu znalezienia maksymalnej rangi wśród elementów z tablicy T,
#pierwszą pętlą for wybieram element dla którego będę sprawdzał
#rangę, w drugiej pętli sprawdzam ile jest elementów znajdujących się
#przed nim o wartości mniejszej od niego. Jeśli taki element znajdę
#zwiększam cnt o 1, następnie po zakończeniu drugiej pętli aktualizuję
#największą aktualnie znalezioną rangę, jeśli znaleziono większą.
#Ostatecznie max_rank to maksymalna ranga pośród wszystkich elementów
#tablicy.
#Złożoność czasowa O(n^2)
#Złożoność pamięciowa O(n)
from kol1testy import runtests

def maxrank(T):
    n = len(T)
    max_rank = 0
    for i in range(n):
        cnt = 0
        for j in range(i):
            if T[j] < T[i]:
                cnt += 1
        if cnt > max_rank: max_rank = cnt
    return max_rank

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
