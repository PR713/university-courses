
def longest(T):
    n = len(T)
    i = 0
    max_len = 0
    while i < n-1:
        q = 0 if T[i][0] == 0 else (T[i+1][0]/T[i+1][1])/(T[i][0]/T[i][1])
        curr_len = 1
        while i < n-1 and (T[i][0]/T[i][1]) * q == (T[i+1][0]/T[i+1][1]):
            curr_len += 1
            i += 1
        i += 1 #musi być w drugim while też od 'i' żeby szukało ciągu również od jakiegoś momentu
        max_len = max(max_len, curr_len)
    return max_len if max_len > 2 else 0

print(longest([(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)])) #wypisze 4
print(longest([(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)])) #wypisze 3
print(longest([(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)])) #wypisze 6
print(longest( [(1,2),(2,3),(3,4),(4,5),(5,6)] )) #wypisze 0
print(longest( [(0,1),(0,2),(0,3),(0,4)])) #wypisze 4


