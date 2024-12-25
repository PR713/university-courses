#Implementacja funkcji sprawdzającego czy graf ma cykl
from collections import deque
#M macierzowo
def cycle(M):
    n = len(M)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = deque()
    Q.append(0)
    visited[0] = True
    while Q:
        s = Q.popleft()
        for i in range(n):
            if M[s][i] == 1:
                if visited[i] == True and parent[s] != i:# żeby się nie cofać
                    return True
                if not visited[i]:
                    visited[i] = True
                    parent[i] = s
                    Q.append(i)
    return False

S=[[0, 1, 0, 0],
   [1, 0, 4, 0],
   [0, 4, 0, 3],
   [0, 0, 3, 0]]
print(cycle(S))
