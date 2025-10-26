

a = int(input('Podaj liczbę: '))
b = 2  # od 2 bo suma zawsze = 1 i nie chcemy liczyć oprócz 1 też 12 s = s+a//...
s = 1
# podzielniki właściwe 12 to 1,2,3,4,6 - bez 12
while b*b < a: # nie może być <= bo wtedy dwa razy liczy b dla 4,9,16,25...
    if a % b == 0:
        s = s + a//b + b   # np 12//3 to 4 ale ma też dopisać b więc + b = +3
    b += 1

if b*b == a:
   s += b

print(s)