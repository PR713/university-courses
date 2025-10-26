def zad32(T, k):
    def rec(k, i, fir, fi, sec, si):
        if fi != 0 and fi == si and fir == sec == k:
            return True
        elif i == len(T):
            return False
        else:
            return rec(k, i + 1, fir, fi, sec, si) or rec(k, i + 1, fir + T[i], fi + 1, sec, si) or rec(k, i + 1, fir,
                                                                                                        fi, sec + T[i],
                                                                                                        si + 1)
    return rec(k, 0, 0, 0, 0, 0)


print(zad32([2, 1, 3, 7, 0], 4))