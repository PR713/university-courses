#Zaczynamy w jakimś dniu zerowym
#T = {t1,...,tn} zadania
#d(ti) naturalne, termin końcowy deadline
#dla zadania t_i
#g(ti) naturalne, zysk
#Chcemy znaleźć taki podzbiór zadań żeby
#zyskać jak najwięcej max zysk, wykonanie każdego zadania
#to 1 dzień

#posortować zadania od największego do najmniejszego zysku
#!! czasami nie musi się opłacać zadania w deadline
#bierzemy ostatni dzień i spośród nich które można wykonać
def tasks(D,G):
    n = len(G) #=len(D)
    idx = [i for i in range(n)]
    idx.sort(key = lambda i: G[i], reverse = True)
    timeline = [False for _ in range(max(D))] #od 0 do max deadline
    gain = 0
    done = []
    for i in idx: #tylko po to żeby dodawać zyski od najwiekszych
        #niżej jako += G[i]
        for j in range(D[i]-1,-1,-1):
            if not timeline[j]:
                timeline[j] = True
                gain += G[i]
                done.append(i)
                break
        #więc jakby tylko patrzymy który timeline już zajety i
        #ustawiamy go jak nadalej jego deadline pozwala, żeby
        #dać innym szansę jeśli miałyby krótszy
    return done,gain

#lub na pewno poprawne
#bierzemy ostatniego dnia najbardziej zyskowne,
#reszcie deadline o 1 mniej i rekurencja/iteracja