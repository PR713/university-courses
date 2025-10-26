#wypisuje ile razy powtarza się wyraz w napisie
def multi(T):
    max_len = 0
    for napis in T:
        n = len(napis)
        i = 1
        l = 1
        length = 1
        while i <= n/2:
            if n % i == 0:
                while i * l < n:
                    if napis[0:i] == napis[i * l: i * (l+1)]:
                        length += 1
                        l += 1
                    else: break
                if i * l == n:
                    max_len = max(max_len, length)
            i += 1
    return max_len

T=["ABCABCABC","ABABABAB"]
print(multi(T)) # 4
