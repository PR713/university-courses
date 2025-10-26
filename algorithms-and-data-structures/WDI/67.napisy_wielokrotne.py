def czy_wielokrotne(s):
    n = len(s)
    l = 1
    while l <= n/2:
        if n % l == 0:
            seq = s[0:l]
            i = 1
            while i * l < n:
                next_seq = s[i*l:(i+1)*l]
                if next_seq != seq:
                    break
                i+= 1
            else:
                return True
        l += 1
    return False

def zad2(T):
    n = len(T)
    max_len = 0
    for s in T:
        if (czy_wielokrotne(s)):
            max_len = max(max_len, len(s))
    return max_len
