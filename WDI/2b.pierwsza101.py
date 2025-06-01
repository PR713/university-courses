def suma(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

def prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

first, s, l = 0, 0, 0
while s < 101: # skończy na 101, ze znakiem <= przeszła by pętla i s = 102
    x = min(9, 101 - s)
    #print(x)
    s += x # 9*11 to 99, 101-99 daje x = 2 ale od końca więc x = 9, 11 razy i potem x = 2 więc
    first += 10**l * x # dodaje 9+99+...+99999999999 + liczbę z cyfrą o l+1 bo l+=1 i to daje '2' na początku :)
    #print(first)
    l += 1 # pierwsza taka liczba co ma sume 101 to 9*11 -> 299999999999

while not prime(first):
    add = 9
    while suma(first + add) != 101:  # gdy będzie równa 101 pętla się przerwie
        add *= 10  # po pierwszym razie 29..99 + 90...0 i powstaje 3899..99
        # print(first) w pamięci jest zapisana stricte poprzednia liczba i pokazuje co raz mniej razy
        # poprzednią liczbę bo mniej razy się wykonuja pętla
    first += add # w tym momencie mamy first = 3899...9 potem do tego dodajemy już nie 9000 tylko 900,90,9
    #print(first)# bo szybciej przerwie się druga pętla bo suma będzie 101 i przesuwa się "8" w liczbie
print(first)