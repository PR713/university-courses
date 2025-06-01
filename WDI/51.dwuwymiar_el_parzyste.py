#czy istnieje wiersz w tablicy gdzie każda z liczb zawiera min. jedna cyfrę parzystą.

def parzyste(T):
    n = len(T) #ilość wierszy
    m = len(T[0]) #może też być T[1], T[2], o indeksy wierszy 0,1,2 i zwraca ilość kolumn w pionie = 4
    for j in range(n):
      cnt_parz = 0
      for i in range(m):
          cyfra = 0
          while T[j][i] > 0:
              cyfra = T[j][i] % 10
              if cyfra % 2 == 0: #czyli cyfra parzysta
                  cnt_parz += 1
                  break #bo znalazło już w danym elemencie parzystą i patrzy na i = 1,2,...
              T[j][i] //= 10

          if cnt_parz == m:#liczba el. z min 1 parzystą jest równa liczbie el. w tablicy w wierszu
              return f'W {j} wierszu każdy element ma min jedną cyfrę parzystą :)'
    return f'W żadnym wierszu nie ma liczb z min jedną cyfrą parzystą'

T = [[1,3,5,7],[3,5,7,11],[22,4,12,21]]
print(parzyste(T))
