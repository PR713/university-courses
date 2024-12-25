# Mówimy, że v jest uniwersalnym ujściem grafu skierowanego,
# jeśli każdy inny wierzchołek ma krawędź do v, a v nie ma
# żadnej wychodzącej, G - dany macierzowo
# Należy sprawdzić czy G ma uniwersalne ujście
# 0-1-2-u-4 wierzchołki
# 0,0,0,1,0 -0
# 0,0,0,1,0 -1
# 0,0,0,1,0 -2
# 0,0,0,0,0 -u
# 0,0,0,1,0 -4 trzeba znaleźć słup jedynek w pionie
# poza jedną i zer w poziomie
# 0 - idziemy w prawo, 1 - w dół O(n)
# startujemy z lewego górnego rogu i uderzymy albo w kolumnę
# tą pionową albo poziomą i już dolecimy zerami do prawej krawędzi
#i potem weryfikujemy czy jest to poprawne bo może znaleźć
#niepoprawne, ale jeśli tak to znaczy że nie istnieje rozwiązanie
# (bo jak uderzymy to już będziemy wędrować tą kolumną albo wierszem
# i potem zerami w prawo do brzegu tablicy)
# po prostu for ... dla kolumny i niżej drugi for dla wiersza
# znalezionych, bo mamy numer wierzchołka więc bez problemu

# lub O(n^2) można sumy szukać

def ujscie(G):  # macierzowo 1 - krawędź, 0 brak jej
    i, j = 0, 0
    n = len(G)
    while i != n and j != n:
        if G[i][j] == 1:
            i += 1
        else:  # == 0
            j += 1

    if i == n:
        return False #bo doszło do ostatniego wiersza
    #i nie doszło do prawej krawędzi macierzy zerami

    for k in range(n):
        if k == i: continue #to jedno 0 pośród kolumny jedynek
        if G[k][i] == 0: return False #jeśli wcześniej gdzieś 0 to False

    for k in range(n):
        if G[i][k] == 1: return False #jeśli gdzieś 1 to False
    return (True,i)

G = [[0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]]
print(ujscie(G))