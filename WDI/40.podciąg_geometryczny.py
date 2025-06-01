tab = [1,4,8,11,15,30,60,120,19,240,23,27,31,35,27,]
licznik = 1
x = 1
for j in range(-5,5): #iloraz ciągu lub iloraz = a[i]/a[i-1]...
   for i in range(1,len(tab)):
     if tab[i] == tab[i-1]*j:
         licznik += 1 #po pierwszym znalezieniu = 2 jako dwuwyrazowy ciąg
         if licznik > x:
             x = licznik
     else:
         licznik = 1 #jeśli podciąg się kończy
   licznik = 1
print(x)