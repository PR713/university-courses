def skroc_ulamek(l, m):
    temp1, temp2= l, m
    while m > 0:
        l, m= m, l % m #skracanie - dzielenie przed nwd(l,m)
    #end while

    return temp1 // l, temp2 // l

def il25(m):
    pom = m
    i = 2
    counter_2, counter_5 = 0, 0

    while pom % 2 == 0:
        counter_2 += 1
        pom = pom // 2
    #end while 1

    while pom % 5 == 0:
        counter_5 += 1
        pom = pom // 5
    #end while 2

    if counter_2 >= counter_5: return counter_2
    else: return counter_5
# Ilosc miejsc po przecinku bez okresu to max( ilosc dwojek, ilosc piatek w rozkladzie na czynniki pierwsze)
def ulamek(l, m):
    l, m = skroc_ulamek(l, m)
    print( l // m, end="")
    l = l % m
    if l > 0:
        print(".", end="")
        for _ in range( il25(m) ):
            l *= 10
            print( l//m, end="")
            l = l % m
        #end for
        if l > 0:
            print("(", end="")
            mem = l
            while True:
                l *= 10
                print( l//m, end="")
                l = l % m
                if l == mem: break #jeśli reszta z dzielenia będzie taka sama
            #end while #tak sie nigdy nie stanie w przeciwieństwie do l//m dla każdego l < m... albo wielokrotności m < l < 2m...
            print(")", end="")
        #end if
    print()

l = int(input('Podaj pierwszą liczbę: ') )
m = int(input('Podaj drugą liczbę: ') )
ulamek(l, m)

















"""a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))
liczba_po_przecinku = 0
liczba_drugi_przypadek = 0
i = 0
liczba = 1
x = a//b
a1 = a//10 #żeby porównywać czy ułamek ma okres zaczynający się od
b1 = b//10 #dalszego miejsca
while i < 15:
    a %= b
    a *= 10
    liczba_po_przecinku += (a//b) * 10**i
    liczba = liczba_po_przecinku
    if b1 > a1:
      x1 = liczba_po_przecinku
      a %= b
      a *= 10
      liczba_po_przecinku = (a // b)

      while i < 15:
          a %= b
          a *= 10
          liczba_po_przecinku += (a // b) * 10 ** (i+1)
          liczba = liczba_po_przecinku
          #print(liczba_po_przecinku)
          i += 1
          for j in range(15):
              if liczba_po_przecinku != 0 and liczba_po_przecinku == liczba_po_przecinku // (10 ** j) + (liczba_po_przecinku // 10 ** j) * (10 ** j):
                  liczba_po_przecinku = liczba_po_przecinku // (10 ** j)
                  print(f'{x}.{x1}', end="(")
                  while j >= 1:
                      a %= b
                      a *= 10
                      print(a // b, end="")
                      j -= 1
                  print(')')
                  quit(0)
          else:
              a1 = 10 * (a % b)
              if a // b == a1 // b:
                  for k in range(i + 1):
                      liczba_po_przecinku %= 10
                      liczba_drugi_przypadek += liczba_po_przecinku
                      liczba_po_przecinku //= 10

                  if liczba_drugi_przypadek == a // b:
                      print(f'{x}.({(a // b)})')
                      quit(0)
                  else:
                      print(f'{x}.{liczba_drugi_przypadek}({(a // b)})')
                      quit(0)

    for j in range(15):
      if liczba_po_przecinku!= 0 and liczba_po_przecinku == liczba_po_przecinku//(10**j) + (liczba_po_przecinku//10**j)*(10**j):
        liczba_po_przecinku = liczba_po_przecinku//(10**j)
        print(x, end =".(")
        while j >= 1:
            a %= b
            a *= 10
            print(a//b, end ="")
            j -= 1
        print(')')
        quit(0)
    else:
        a1 = 10*(a%b)
        if a//b == a1//b:
            for k in range(i+1):
               liczba_po_przecinku %= 10
               liczba_drugi_przypadek += liczba_po_przecinku
               liczba_po_przecinku //= 10

            if liczba_drugi_przypadek == a//b:
                print(f'{x}.({(a // b)})')
                quit(0)
            else:
                print(f'{x}.{liczba_drugi_przypadek}({(a//b)})')
                quit(0)
    i+=1"""
