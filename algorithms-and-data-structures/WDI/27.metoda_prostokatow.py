
k = int(input('Podaj koniec przedziału: '))
poczatek_przedzialu = 1
n = int(input('Podaj dokladność: '))
dokladnosc = (k-poczatek_przedzialu)/n #podstawa każdego prostokąta po 'x'ach
pole_prostokata = 0
calka = 0 #funkcja 1/x

for i in range(1,n): #przedział podzielony na 'n' części
    calka += (1/(poczatek_przedzialu + i*dokladnosc))*dokladnosc
print(calka)