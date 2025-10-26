"""def przelicznik_systemy(x,s):
   liczba = ''
   x1 = x
   while x > 0:
     cyfra = x % s
     x //= s
     if cyfra >= 10:
        cyfra -= 10
        liczba = chr(ord('A') + cyfra) + liczba
     else:
        liczba = str(cyfra) + liczba
   print(f'Liczba {x1} w systemie {s} to: {liczba}')

x = int(input('Podaj liczbę: '))
s = int(input('Na jaki system ją zamienić 2...16? '))
print(przelicznik_systemy(x,s))"""  # funkcja zamieniająca na wybrany system liczbowy


# Można też porównywać po każdym znaku ale już użyć lepiej tablicy, szybciej
def digit(a, b, system):
    dig = [False for _ in range(system)]
    while a > 0:
        dig[a % system] = True
        a //= system
    while b > 0:
        if dig[b % system]:
            return False
        b //= system
    return True


def systemyliczbowe(a, b):
    for i in range(2, 17):
        if digit(a, b, i):
            return i
    return 'Nie istnieje taki system liczbowy'


print(systemyliczbowe(123, 522))
