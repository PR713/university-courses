
tab = [1,3,5,7,9,11,23,11,15,19,23,27,31,35,27,]
licznik = 1
x = 1
for j in range(-10,10): #różnica ciągu lub roznica = a[i] - a[i-1]
   for i in range(1,len(tab)):# i potem czy dla i+=1 też a[i]-a[i-1] = roznicy
     if tab[i] == tab[i-1] + j:
         licznik += 1 #po pierwszym znalezieniu = 2 jako dwuwyrazowy ciąg
         if licznik > x:
             x = licznik
     else:
         licznik = 1 #jeśli podciąg się kończy
   licznik = 1
print(x)
