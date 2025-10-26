#funkcja szukająca największej liczby pierwszej o różnych cyfrach
#powstałej przez ucięcie M-początkowych i N-końcowych cyfr
def pierwsza(x):
    if x < 2: return False
    if x == 2 or x == 3: return True
    if x % 2 == 0 or x % 3 == 0: return False
    i = 5
    while i*i <= x:
        if x % i == 0: return False
        i += 2
        if x % i == 0: return False
        i += 4
    return True

def ile_cyfr(a): #i od razu sprawdza jakie cyfry
    cnt = 0
    while a > 0:
        a//=10
        cnt+= 1
    return cnt

def rozne_cyfry(b):
    dig = [0 for _ in range(10)]
    while b > 0:
       dig[b % 10] += 1
       b//= 10
    #end while
    for digit in dig:
       if digit > 1: return False
    return True #czyli ma różne cyfry

def obcinanie(K):
    cnt = ile_cyfr(K)
    szukana = 0
    for m in range(cnt,0,-1): #obcinanie M początkowych cyfr
        x = K #kopia żeby się nie zmianiała liczba
        x %= 10**(m)  # obcinanie od przodu od 0,1... do cnt-1 cyfr
        a = x
        for n in range(m): #N końcowych
           x //= 10**(n) #obcinanie od tyłu od 0 do cnt-1
           if pierwsza(x) and rozne_cyfry(x):
               if x > szukana:
                   #print(szukana)
                   szukana = x
           x = a
    return szukana

#print(obcinanie(1202742516))