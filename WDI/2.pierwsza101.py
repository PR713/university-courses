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
#można zacząć od n = 2 ale taka liczba musi mieć co najmniej
# tyle cyfr 9*11 - 11 cyfr dużo to nie pomaga
n = 399999900000
while n:
    if suma(n) == 101 and prime(n) == True:
        print(f'Szukana liczba pierwsza o sumie cyfr 101 to: {n}')
        break
    else:
        print(f'Szukam liczby: {n}')
        n+=1


