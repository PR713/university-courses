def dominance(P):
    n = len(P)
    x_count = [0 for _ in range(n+1)]#bo współrzędne od 1...n włącznie
    y_count = [0 for _ in range(n+1)]
    x_prefix_sum = [0 for _ in range(n+1)]
    y_prefix_sum = [0 for _ in range(n+1)]

    for x,y in P:
        x_count[x] += 1
        y_count[y] += 1
    for i in range(1,n+1):
        x_prefix_sum[i] = x_prefix_sum[i-1] + x_count[i]
    #na i-tym indeksie ilość punktów który których
    #współrzędne x <= i
        y_prefix_sum[i] = y_prefix_sum[i-1] + y_count[i]

    max_strength = 0
    for x,y in P:# [x-1] bo dominujące mają < x,y o 1
        s = x_prefix_sum[x-1] + y_prefix_sum[y-1] - n + 1
        #niektóre punkty są zliczone dwa razy, raz w x_prefix
        #raz w y_prefix, więc na ogół s może być < 0
        #ale dla dominującego punktu będzie to zawsze dokładnie n
#n = x_pref_sum + y_pref_sum - zdominowane(xiy pref) + maks. dominujący
#i które dominują obecny, dla maksymalnie dominującego żaden go nie
#dominuje, bo wtedy by oznaczało, że nie jest on maksymalnie dominującym,
#więc tylko on jest w tym zbiorze
#n = X + Y - XiY + D = X + Y - XiY + 1
#stąd s = XY = X + Y - n + 1
        max_strength = max(max_strength,s)

    return max_strength

T = [(1, 3), (3, 4), (4, 2), (2, 2)] #2
#T = [(1,1),(2,2),(3,3),(4,4)] #3
print(dominance(T))

