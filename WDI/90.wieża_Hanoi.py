
def zad14(n):
    def przenies(p, q):
        kijek = ['a', 'b', 'c']
        print(kijek[p], "->", kijek[q])
    def rek(n,a,b,c):
        if n > 1: rek(n-1,a,c,b)
        przenies(a,c)
        if n > 1: rek(n-1,b,a,c)
    rek(n,0,1,2)

print(zad14(4))

