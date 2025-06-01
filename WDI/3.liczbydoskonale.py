def perfect_number(n):
    i = 2
    sum = 1 #żeby nie zliczało 1 i n tylko samą 1 i zaczynało z i = 2
    while i * i < n:
        if n % i == 0:
            sum = sum + i + n//i
        i += 1
    if i*i == n:
        sum += i
    return sum

n = 2 # kolejne liczby doskonałe to 6,28,496,8128 potem 33550336... XD
while n:
    #print(n)
    if perfect_number(n) == n:
        print(f'Liczba doskonała: {perfect_number(n)} ')
    n+=1
    if n > 1000000: quit(':)') #bo kolejna bardzo duża