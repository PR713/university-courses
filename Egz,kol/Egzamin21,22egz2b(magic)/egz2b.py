from egz2btesty import runtests
#f(i) = dotarcie do komnaty i z maks. liczbą złota

def magic( C ):
    n = len(C)
    dp = [ -1 for _ in range(n)]
    dp[0] = 0
    for i in range(n):
        for j in range(1,4):
            curr = i
            next = C[i][j][1]
            skrzynia_curr = C[i][0]
            koszt_do_next = C[i][j][0]#otwierają się jeśli w skrzyni znajdzie się dokładnie C[i-1][j][0] złota
            if dp[curr] != -1 and curr < next and skrzynia_curr - koszt_do_next <= 10 and next != -1:
                dp[next] = max(dp[next], dp[curr] + skrzynia_curr - koszt_do_next)
    return dp[n-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )

"""
def magic( C ): #O(n)
    n = len(C)
    dp = [ -1 for _ in range(n)]
    dp[0] = 0
    for i in range(1,n):
        for j in range(1,4):#otwierają się jeśli w skrzyni znajdzie się dokładnie C[i-1][j][0] złota
            if dp[i-1] != -1 and i - 1 < C[i-1][j][1] and C[i-1][0] - C[i-1][j][0] <= 10 and next != -1:
                dp[C[i-1][j][1]] = max(dp[C[i-1][j][1]],dp[i-1] + C[i-1][0] - C[i-1][j][0])
    return dp[n-1]"""