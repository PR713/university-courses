# pokrycie kolorów
# A - tablica n - elementowa 0,...,k
# Znaleźć najmniejszy spójny fragment
# w którym są wszystkie kolory

def colors(T, k):
    n = len(T)
    start = 0
    min_len = float('inf')
    distinct_count = 0
    count = [0] * k
    min_start, min_end = -1, -1
    for i in range(n):
        count[T[i]] += 1 #zlicza kolory
        if count[T[i]] == 1:
            distinct_count += 1 #zlicza ile różnych kolorów mamy
        while distinct_count == k:
            if i - start + 1 < min_len:#czy odstęp między indeksami
            #jest mniejszy niż poprzedni znaleziony
                min_len = i - start + 1
                min_start, min_end = start, i
                if min_len == k: return (min_start, min_end)
            count[T[start]] -= 1
            if count[T[start]] == 0:
                distinct_count -= 1
            start += 1
    return (min_start, min_end) if min_len != float('inf') else (-1, -1)

print(colors([1,1,1,0,2,3,2,0,1,1],4))