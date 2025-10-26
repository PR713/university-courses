tab = [1,5,7,11,17,27,29,31,33,13,15,57,53,23] #dla r> 0 : 4, dla r< 0: 2

licznik1 = 1
licznik2 = 1
x1 = 1
x2 = 1
for j in range(1,10): #dla różnicy > 0
   for i in range(1,len(tab)):
     if tab[i] == tab[i-1] + j:
         licznik1 += 1 #po pierwszym znalezieniu = 2 jako dwuwyrazowy ciąg
         if licznik1 > x1:
             x1 = licznik1
     else:
         licznik1 = 1 #jeśli podciąg się kończy
   licznik1 = 1

for j in range(-10,0): #dla różnicy > 0
   for i in range(1,len(tab)):
     if tab[i] == tab[i-1] + j:
         licznik2 += 1 #po pierwszym znalezieniu = 2 jako dwuwyrazowy ciąg
         if licznik2 > x2:
             x2 = licznik2
     else:
         licznik2 = 1 #jeśli podciąg się kończy
   licznik2 = 1

print(x1,x2)
print(f'Różnica między długością rosnącego a malejącego ciągu arytm. to {x1-x2}')
