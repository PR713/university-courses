n = float(input('Podaj liczbę po przecinku, którą chcesz zamienić na system binarny: '))
print(0, end='.')
for i in range(10):
    n *= 2
    if n < 1:
        print(0, end = '')
    else:
        print(1, end = '')
        n %= 1
        if n == 0:
            quit(0)

