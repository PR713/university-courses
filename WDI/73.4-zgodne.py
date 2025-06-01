
def cztero_zgodne(a):
    dig = [0 for _ in range(4)]
    while a > 0:
        dig[a%4] = True
        a //= 4
    return dig

def funkcja(T):
    n = len(T)
    max_dlugosc = 1
    for i in range(n-1):#ciag może być niespójny zatem dwie pętle
       cnt = 1
       for j in range(i+1,n):
          if cztero_zgodne(T[i]) == cztero_zgodne(T[j]):
              cnt += 1 #^^ składają się z takich samych cyfr
          if cnt > max_dlugosc:
              max_dlugosc = cnt
    return max_dlugosc

T = [13,23,18,57,7,1,4,57,23,7] #7,13,23 spełniają
#T = [1,2,57,57,57,57,3,57,57]
print(funkcja(T))