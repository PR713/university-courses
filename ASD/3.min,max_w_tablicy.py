
#Znajdź w tablicy liczb T min i max (optymalna liczba porównań)

def min_max(T):
    max = -float('inf')
    min = float('inf')
    for i in T:
        if i > max: # 2n porównań
            max = i
        if i < min:
            min = i
    return (min,max)

def min_max_(T): #szukamy w parach
    s = T[-1]
    m = T[-1] # [-1] bo może nie mieć pary
    n = len(T)
    for i in range(1,n,2):
        if T[i] < T[i-1]:
            n_min, n_max = T[i], T[i-1]
        else:
            n_min,n_max = T[i-1], T[i]
        s = min(s,n_min)
        m = max(m,n_max) # 3n/2 porównań
    return s,m
