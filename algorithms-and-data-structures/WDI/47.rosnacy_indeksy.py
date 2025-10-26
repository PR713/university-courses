
T = [1,3,1,3,5,6,9,11,15,6,9,10,17] #[..1,3,5...] = indeksy 2+3+4 = 9, dłuższy [6,9,10,17] suma = 42
def ciag_rosnacy(T):
    n = len(T)
    max_dlugosc = 0
    for i in range(n-1):
        cnt = 1
        suma_el = T[i]
        suma_indeksów = i
        if T[i+1] > T[i]:
            for j in range(i+1,n):
                if not T[j-1] < T[j]:
                    break
                else:
                    cnt += 1
                    suma_el += T[j]
                    suma_indeksów += j
                    if suma_el == suma_indeksów:
                        max_dlugosc = max(max_dlugosc,cnt)
    return max_dlugosc

print(ciag_rosnacy(T))





