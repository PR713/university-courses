
#Dana jest tabela kursów walut, G[i][j]
#oznacza kwotę waluty i, jaką trzeba zapłacić
#za 1 jednostkę waluty j. Sprawdzić czy istnieje
#waluta 'z' taka, że z 1 jednostką 'z' w ciągu
#wymian uzyskany > 1 jednostkę 'z'

#bierzemy log(1/x) żeby mieć ujemne wagi
#te przeliczniki
#G[zl][eur] = 4,53
#G[eur][zl] = 0,3
#wychodzący na 'zero' to przelicznik G[eur][zl] = 1/G[zl][eur] ~ 0,19
#im wyższa tym dla nas bardziej opłacalne
#mnożymy zl -> eur * eur -> zl... i ten iloczyn ma wyjść > 1

#tu bez log
#tradycyjny Bellman Ford V*V*e = O(VE)
#tutaj od razu V*E = O(VE) bo currencies to możliwe
#wszystkie krawędzie (przeliczniki/krawędzie)
#tylko zgodnie z kolejnością z 0 do wszystkich sąsiadów,
#z 1 do reszty itd. zamiast for O(V) ... for O(e)

def relax(currencies, cost, parent, j):
    if cost[currencies[j][1]] < currencies[j][2] * cost[currencies[j][0]]:
        cost[currencies[j][1]] = currencies[j][2] * cost[currencies[j][0]]
        #tzn ile najwięcej danej waluty można dostać z różnych przeliczników
        if currencies[j][0] == parent[currencies[j][1]]: #czyli już został znaleziony cykl
        #o dodatniej wadze, w której możemy zarobić, bo znaleziono raz cost mniejszy
        #a teraz większy
            return True
        parent[currencies[j][1]] = currencies[j][0]
    return False

def currency_exchange(currencies):
    max_vertex = 0
    for i in range(len(currencies)):
        max_vertex = max(max_vertex, currencies[i][0], currencies[i][1])
    E = len(currencies)
    cost = [0] * (max_vertex + 1)
    parent = [None] * (max_vertex + 1)
    cost[0] = 1
    for i in range(max_vertex - 1):
        for j in range(E):
            if relax(currencies, cost, parent, j):
                return True
    return False


currencies = [(0, 1, 4.5),
              (0, 2, 4),
              (0, 3, 0.4),
              (1, 2, 0.75),
              (2, 0, 0.25),
              (3, 2, 100),
              (3, 4, 2)]
print(currency_exchange(currencies))

PLN = 0; EUR = 1; USD = 2; YEN = 3;

K = [(PLN, EUR, 4.51), (PLN, USD, 3.68), (PLN, YEN, 0.034),
     (EUR, PLN, 0.22), (EUR, USD, 0.82), (EUR, YEN, 0.0075),
     (USD, PLN, 0.27), (USD, EUR, 1.22), (USD, YEN, 0.0091),
     (YEN, PLN, 29.83), (YEN, EUR, 133,47), (YEN, USD, 109.62)]
print(currency_exchange(K))

#tutaj po prostu patrzymy czy raz dotarliśmy przelicznikiem
#mniejszym a potem nagle większym po tej samej wymianie
#ten sam parent i potomek, czyli cykl dodatni - zarabiamy :)
#a na bit - można dzielić przez converter i sprawdzić czy cost>1