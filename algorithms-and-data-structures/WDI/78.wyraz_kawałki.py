
def czy_samogloska(ch):
    return ch in ['a', 'e', 'y', 'u', 'i', 'o']

def cutting(s):
    n = len(s)

    def rek(i,cnt):
        if i == n:
            return cnt

        if czy_samogloska(s[i]):
            cnt += 1

        if cnt == 2:
            return 0
        elif cnt == 1:
            return rek(i+1, 0) + rek(i+1,1)

        return rek(i+1,0) #czyli jeśli cnt == 0 to
    return rek(0,0)

print(cutting('sesja'))
