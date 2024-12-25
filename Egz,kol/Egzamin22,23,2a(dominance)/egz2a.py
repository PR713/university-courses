from egz2atesty import runtests


def dominance(P):
    n = len(P)
    x_cnt = [0] * (n+1)
    y_cnt = [0] * (n+1)
    x_prefix = [0] * (n+1)
    y_prefix = [0] * (n+1)

    for x,y in P:
        x_cnt[x] += 1
        y_cnt[y] += 1

    for i in range(1,n+1):
        x_prefix[i] = x_prefix[i-1] + x_cnt[i]
        y_prefix[i] = y_prefix[i-1] + y_cnt[i]

    d = 0
    for x,y in P:
        d = max(d,x_prefix[x-1]+y_prefix[y-1] - n + 1)
    return d


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(dominance, all_tests=True)
