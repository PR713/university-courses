from kol1testy import runtests

def maxrank(T):
    max_rank, max_el = 0, -1
    for i in range(len(T)-1,-1,-1):
        if T[i] > max_el:
            max_el = T[i]
            max_rank = max(max_rank, len([None for num in T[:i] if num < T[i]]))
    return max_rank
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )