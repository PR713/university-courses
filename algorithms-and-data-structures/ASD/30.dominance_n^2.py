
def dominance(P):
    n = len(P)
    cnt_max = 0
    for i in range(n):
        cnt = 0
        ind = i
        for j in range(n):
            if j != i and P[i][0] > P[j][0] and P[i][1] > P[j][1]:
                cnt += 1
        if cnt > cnt_max:
            cnt_max = cnt
    return cnt_max
