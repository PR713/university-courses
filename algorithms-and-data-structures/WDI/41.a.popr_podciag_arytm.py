
T = [1,5,7,11,17,27,29,31,33,13,15,57,53,49,23] #dla r> 0 : 4, dla r< 0: 3

def check(T):
    n = len(T)
    cnt_r1 = 2
    cnt_r2 = 2
    cnt = 0
    for i in range(1,n-1):
        for j in range(i+1,n):
            if T[i] - T[i-1] == T[j] - T[i]:
                cnt = 3
                r = T[i] - T[i-1]
                a = j
                while a + 1 < n:
                    if T[a+1] - T[a] == r:
                        cnt += 1
                        a += 1
                    else: break
                if r > 0 and cnt > cnt_r1:
                    cnt_r1 = cnt
                if r < 0 and cnt > cnt_r2:
                    cnt_r2 = cnt
    return cnt_r1, cnt_r2

print(check(T))
