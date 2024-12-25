
def parzyste(T):
    s, ans, cnt = 0, 0, [1, 0]
    for x in T:
        s += x
        ans += cnt[s % 2]
        cnt[s % 2] += 1
    return ans