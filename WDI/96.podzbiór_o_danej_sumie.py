
def zad21(T,S):
    n = len(T)
    def rek(T,S,s,k,w):#k,w tablice przechowujace False/True czy można
        if s > S: #jeszcze wziąć element z danej kolumny lub wiersza
            return False
        if s == S and s != 0:
            return True

        for y in range(3):
            if w[y]:
                for x in range(3):
                    if k[x]:#obie True czyli można wziąć z danej pary w,k
                        w[y],k[x] = False, False
                        if rek(T,S,s+T[y][x],k,w):
                            return True #bez tego if zwróci pierwsze lepsze
# czyli może być False a True mogłoby nadal wystąpić i patrzy zarówno
# na warunek końcowy jak i tu poniżej na False,
# bo wywołujemy w ifie a bez if'a właśnie by zakończyło jak popadnie,
# a tutaj tylko czyha na to czy będzie True
                        else:
                            w[y], k[x] = True, True

        return False
    return rek(T,S,0,[True]*3,[True]*3)

T = [[1,2,3],
     [2,2,2],
     [3,1,1]]

print(zad21(T,8))