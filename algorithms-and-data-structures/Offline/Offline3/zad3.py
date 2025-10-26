#Radosław Szepielak
#Tworzę 4 listy. Lista x_count zlicza na i-tej współrzędnej ile
#jest punktów których x = i, analogicznie dla y_count. Natomiast
#x_prefix_sum zlicza na i-tej współrzędnej ile jest punktów których
#x jest <= i - analogicznie dla y_prefix_sum. Niektóre punkty są
#zliczone dwa razy, raz w x_prefix raz w y_prefix, więc na ogół s
#może być < 0 ale dla dominującego punktu będzie to zawsze dokładnie
#n = x_pref_sum + y_pref_sum - zdominowane + (maksymalnie dominujący
# i które dominują obecny) dla maksymalnie dominującego żaden go nie
#dominuje, bo wtedy by oznaczało, że nie jest on maksymalnie dominującym,
#więc tylko on jest w tym zbiorze D = 1
# n = X + Y - XiY + D = X + Y - XiY + 1
#stąd XiY = s = X + Y - n + 1
#Złożoność czasowa O(n)

from zad3testy import runtests

def dominance(P):
    n = len(P)
    x_count = [0 for _ in range(n + 1)]  # bo współrzędne od 1...n włącznie
    y_count = [0 for _ in range(n + 1)]
    x_prefix_sum = [0 for _ in range(n + 1)]
    y_prefix_sum = [0 for _ in range(n + 1)]

    for x, y in P:
        x_count[x] += 1
        y_count[y] += 1
    for i in range(1, n + 1):
        x_prefix_sum[i] = x_prefix_sum[i - 1] + x_count[i]
        y_prefix_sum[i] = y_prefix_sum[i - 1] + y_count[i]

    max_strength = 0
    for x, y in P:  # x,y naturalne >= 1
        s = x_prefix_sum[x - 1] + y_prefix_sum[y - 1] - n + 1
        max_strength = max(max_strength, s)

    return max_strength
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
