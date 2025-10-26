def sito(n):
    a = [True] * (n+1) # przedział od <0, n> ale n+1 el. w tablicy
    a[0] = False
    a[1] = False
    i = 2
    while i*i <= n:
        if a[i]: #jednoznacze z if True:
            for j in range(i*i, n+1, i):
                #print(i,j) #zawsze i tak trzeba dać i*i<n w while żeby nie sprawdzało większych
                a[j] = False #od i*i
        i+=1
    return a # Dlaczego przechodzimy od razu do komórki i*i? Popatrzmy na liczbę 5, która jest pierwsza.
    # Pierwsze wykreślenie znajduje się pod komórką 5*5 = 25, ponieważ liczby 2*5, 3*5 oraz 4*5
    # złożone są z czynników, które zostały wcześniej wykreślone.

n = 20000
a = sito(n) # przypisujemy do 'a' wartości True or False, dzięki temu mamy dostęp do listy w funkcji
for i in range(n + 1): #można by też bez funkcji zrobić wprost bez tego przypisania
     if a[i] == True: # wyżej range od <0, do n+1) bez n+1
      print(i)
