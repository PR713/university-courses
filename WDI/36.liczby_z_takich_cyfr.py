pierwsza = int(input('Podaj pierwszą liczbę: '))
druga = int(input('Podaj drugą liczbę: '))
pierwsza1 = [0 for _ in range(10)]  # na kolejnych indeksach liczba cyfr od 0 - 9
druga2 = [0 for _ in range(10)]


def dwieliczby(pierwsza, druga):
   while pierwsza > 0:
       a = pierwsza % 10
       pierwsza1[a] += 1
       pierwsza //= 10
   while druga > 0:
       a = druga % 10
       druga2[a] += 1
       druga //= 10
   for i in range(10):
       if pierwsza1[i] != druga2[i]:
           print('Nie składają się z takich samych cyfr :(')
           quit(0)
   return 'Te liczby składają się z takich samych cyfr :)'


print(dwieliczby(pierwsza, druga))
