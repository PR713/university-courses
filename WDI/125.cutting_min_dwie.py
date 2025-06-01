
def samogloski(a):
    return a in ["a","e","i","o","u","y"]

def cutting(s):
    n = len(s)

    def rek(i,cnt=0,licz=0):
        if i == n:
            return licz

        if samogloski(s[i]):
            cnt += 1
        if cnt >= 1:
            return rek(i+1,0,0) + rek(i+1,cnt,1)
        else:
            return rek(i+1,0,0)

    return rek(0,0) - 1

print(cutting("student"))
print(cutting("sesja"))
print(cutting("ocena"))
