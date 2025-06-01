def waga(num):
    cnt = 0
    i = 2
    while num != 1:
        if num % i == 0:
            cnt += 1
        while num % i == 0:
            num //= i
        i += 1

    return cnt

def zad6(T):
    n = len(T)

    def rek(i,a,b,c):
        if i == n:
            return a == b and b == c #True jeśli są równe

        return rek(i+1, a + waga(T[i]), b, c) or rek(i+1, a , b + waga(T[i]), c) or rek(i+1, a , b, c + waga(T[i]))

    rek(0,0,0,0)
