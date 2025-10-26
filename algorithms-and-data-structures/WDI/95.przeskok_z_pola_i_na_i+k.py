
def czy_czynnik_pierwszy(a,b):#a to T[i], b to k
    j = 2
    copy_a = a
    while j*j <= a:
        while a % j == 0:
            if j == b:#gdy nasze b = k nie jest l. pierwszą np k = 4 to i tak a%j==0 nie wykona się git
                return True#więc nie trzeba is_prime(k)
            a //= j
        j += 1
    if a > 1:#albo np dla 15 została "5" albo dla 11 zostało 11 i dla 11 copy_a !=a
        if copy_a != a and a == b: return True #bo ma być mnniejszy od T[i]
    return False

def zad25(T):
    n = len(T)
    def rek(T, i, cnt):
        nonlocal n
        if i == n-1:
            return cnt

        k = 2
        mini = float("inf")
        while i + k < n:
            if czy_czynnik_pierwszy(T[i],k):
                mini = min(mini, rek(T, i + k, cnt + 1))
            k += 1
        return mini

    mini = rek(T, 0, 0)
    return mini if mini != float("inf") else -1
