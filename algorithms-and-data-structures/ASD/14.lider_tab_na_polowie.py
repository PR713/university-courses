
#Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm
# o złożoności O(n), który stwierdza, czy istnieje taka z liczb
# x (tzw. lider A), która występuje w A na ponad połowie pozycji
# aaxaxbxxx, dwie grupy liczb jedna to lider, druga to reszta
# ZSD ponad połowa pozycji więc idea taka że i jeśli
# lider istnieje a tak zakładamy, to i tak jest go więcej
# niż połowa elementów, więc jeśli nawet będzie przerwa
# np 1,1,2,5,3 i cnt zejdzie do 1 i będziemy zamieniać kandydatów
# to w końcu jeszcze raz się wzniesie na poprawnego na cnt >= 1
def lider(T):
    n = len(T)
    candidate = T[0]
    cnt = 0
    for i in T:
        if i == candidate: cnt += 1
        elif cnt == 1: candidate = i
        else: cnt -= 1
    cnt = 0
    for i in T:
        if i == candidate: cnt += 1
    if cnt/n > 0.5: return True
    return False

T = [1,1,2,1,1,2,5,1,2,1,3,1,3,1,7]

print(lider(T))