def tablica(t):
  a = b = 1
  while a < 10: #załóżmy że dana tablica t ma 10 elementów
     cnt = 0
     i = 2
     if t[a] <= 3:
        return print('Nie istnieje') #bo pod tym indeksem = a, nie ma liczby złożonej
     else:
        while i*i <= t[a]:
            if t[a] % i != 0: #sprawdzamy czy nie jest pierwszą, bo ma być złożoną
               i += 1
            else:
              i+= 1
              cnt += 1
        #jeśli 'i' doszło do sqrt i cnt = 0 czyli jest pierwszą
        if cnt == 0:
            return print('Nie zachodzi ten warunek.')

     a,b = b, a+b
  ###teraz sprawdzamy wszystkie na raz czy jest jakakolwiek pierwsza,bo skoro reszta złożona to to nam nie przeszkadza
  cnt_pierwszych = 0
  for j in range(10):#lecimy przez tablicę
      x = t[j]
      i = 2
      while i*i <= t[j]:
          if t[j] % i == 0:#nie jest pierwszą
              t[j] //= i
              break
          i += 1

      if x == t[j] and x >= 2: #czyli się nie zmieniła przy dzieleniu //i to jest pierwszą
          return print('Wszystkie el. z indeksami z ciągu Fib. są złożone, a z reszty min. jedna pierwsza :)')

  return print('Nie jest to spełnione')

#t = [0,4,6, 8,6,12,13,16,11,6]
t = [0,4,6,8,10,15,4,4,18,9] #wariant ze złożonymi na indeksach 'a' ale bez pierwszej poza nimi
tablica(t) #samo wywołanie, bo print(tablica(t)) zwróci to i None