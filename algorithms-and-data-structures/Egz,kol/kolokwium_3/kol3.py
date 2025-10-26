# Radosław Szepielak
from kol3testy import runtests
import json


# Skaluję wartości tablicy T, z T[i] na T[i] % m, żeby trzymać tylko
# informację o reszcie z dzielenia przez m <= 7*n.
# F(i,j,k) = liczba pozostałych jabłek % 7, ciąg pierwszych i drzew,
# wycięto z nich k drzew
# rekurencja
# warunek początkowy F[i][S[i]][0] = True


def orchard(T, m):
    dp = [-1] * m
    dp[0] = 0
    #dp[i] maksymalna ilość drzew które
    #można zostawić dla każdej wartości %m = i
    for v in T:
        nu = dp[:]
        for i in range(m):
            if dp[i] < 0: continue
            j = (i + v) % m
            #czyli z wcześniejszych mamy
            #resztę 'i' a teraz dodatkowo + v
            nu[j] = max(nu[j], dp[i] + 1)
        dp = nu
    return len(T) - dp[0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
