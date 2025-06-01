
def dividers(n):
    i = 2
    divs = []
    while i*i <= n:
        if n % i == 0:
            divs.append(i)
            while n % i == 0:
                n //= i
        i+= 1
    if n != 1:
        divs.append(n)
    return divs

def zad31(n):
    divs = dividers(n)
    Sum = 0

    def rec(prod, i):
        nonlocal Sum
        if i == len(divs):
            Sum += prod
        else:
            rec(prod * divs[i], i + 1)
            rec(prod, i + 1)

    rec(1, 0)
    return Sum - 1

print(zad31(60))