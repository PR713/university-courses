
def przesuwanie(tab,x):
   if x < tab[9]:
       return tab #bez zmian
   for i in range(9,-1,-1):
       if x == tab[i]:
           return tab
       if x > tab[i]:
           indeks = i #zapamiętanie na którym miejscu jest największa mniejsza od x

   for i in range(indeks,10): #spychanie do tyłu
       tab[i],x = x, tab[i]
   return tab

def tablica_liczb():
   tab = [0 for _ in range(10)]
   while True:
       x = int(input())
       if x == 0:
           return tab[9]#wypisuje 10-tą wartość największą
       else:
           tab = przesuwanie(tab,x)
           print(tab)

print(tablica_liczb())