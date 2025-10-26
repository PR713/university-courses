from math import inf
def zad(T):
    mincnt = float('inf')
    sum = 0
    def f(T,suma_el = 0, suma_ind = 0, p = 0, cnt = 0):
        nonlocal mincnt
        nonlocal sum
        n = len(T)
        if suma_el == suma_ind and 0 < cnt < mincnt:#wcześniej niż p == n bo
            mincnt = cnt#najpierw to^^ sprawdza potem return sum jak p == n
            sum = suma_el #trzeba ją zaktualizować wcześniej
        if p == n: return sum
        else:
            f(T,suma_el,suma_ind,p+1)
            f(T,suma_el +T[p], suma_ind + p, p+1, cnt+1)

    f(T)
    return sum

T = [ 1,7,3,5,11,2 ]
print(zad(T))
# 10 lub 8 jak wywołania na odwrót, szybciej znajduje