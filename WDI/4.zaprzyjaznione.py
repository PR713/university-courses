def friend_number_1(n):
    i = 2
    sum1 = 1 #żeby nie zliczało 1 i n tylko samą 1 i zaczynało z i = 2
    while i * i < n:
        if n % i == 0:
            sum1 = sum1 + i + n//i #dzielniki właściwe bez tej liczby
        i += 1
    if i * i == n:
        sum1 += i
    return sum1

n = 2

while n<100000: # jeśli dzielniki 220 dają sumę x = 284 i dzielniki 284 dają sumę 220
    n+=1
    x = friend_number_1(n) #x jest równy sumie dzielników liczby n
    if n < x and friend_number_1(n) == x and friend_number_1(x) == n:
          print(f'Para liczb zaprzyjaźnionych: {n, x} ')


quit('DZIAŁA <3 <3 <3')
