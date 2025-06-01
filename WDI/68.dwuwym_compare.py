def compare(A, B):
    n = len(A)
    for i in range(n):
        if A[i] != B[i]:
            return 1 if A[i] == 1 else -1
    return 0

def distance(T):
    n = len(T)
    max_index = 0
    min_index = 0
    for i in range(1, n):
        if compare(T[i], T[max_index]) == 1:
            max_index = i
        elif compare(T[min_index], T[i]) == 1:
            min_index = i
    return abs(max_index - min_index)