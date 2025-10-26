def nieparz(T):
    n = len(T) #ilość wierszy bo zwraca ilość elementów jak w jednowym. tablicy
    m = len(T[0])#może też być T[1],T[2], bo indeksy wierszy 0,1,2 i zwraca ilość kolumn w pionie = 4
    for j in range(n):
      for i in range(m):
          cnt = 0
          cyfra = 0
          cnt_cyfr = 0
          while T[j][i] > 0:
              cyfra = T[j][i] % 10
              if cyfra % 2 != 0: #czyli cyfra nieparzysta
                  cnt += 1
              T[j][i] //= 10
              cnt_cyfr += 1
          if cnt == cnt_cyfr:
              break #idzie do kolejnego wiersza j = 1,2,... bo  znalazło taką
          if i == m-1 and cnt != cnt_cyfr:
              return False #print(f'Np w {j} wierszu nie ma liczby z cyframi nieparzystymi')
    return True #print(f'W każdym wierszu jest liczba z cyframi nieparzystymi')

T = [[1,3,5,7],[3,5,7,11],[22,4,12,18]]
print(nieparz(T))
