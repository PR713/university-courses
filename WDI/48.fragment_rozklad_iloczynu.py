def najdluższy_fragment(T):
    n = len(T)
    factors = [0] * 1000
    left, right = 0, 0
    max_len = 0
    while right < n:
        if max(factors) <= 1:
            copy_num = T[right]
            d = 2
            while copy_num != 1:
                while copy_num % d == 0:
                    factors[d] += 1
                    copy_num //= d
                d += 1
            right += 1
        else:
            copy_num = T[left]
            d = 2
            while copy_num != 1:
                while copy_num % d == 0:
                    factors[d] -= 1 #usuwamy dzielniki lewego krańca i przesuwamy go jeden w prawo
                    copy_num //= d
                d += 1
            left += 1

        if max(factors) <= 1:
            #print(factors) #dopóki żaden czynnik pierwszy się nie powtórzy
            max_len = right - left
    return max_len

T = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]
print(najdluższy_fragment(T))
