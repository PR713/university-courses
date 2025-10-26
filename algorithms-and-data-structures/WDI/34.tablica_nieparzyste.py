tab = [1,3,7,23,11,15,27]

for i in range(len(tab)):
    cnt = 0
    a = tab[i]
    while a > 0:
       if (a%10)%2 == 0:
         a = a//10
       else:
           cnt += 1
           break #sprawdź kolejną bo ta ma już jedną nieparzystą
    if a == 0 and cnt == 0:
        print(f'Nie, np liczba {tab[i]} nie ma min. jednej cyfry nieparzystej')
        quit(0)
print('Tak, wszystkie elementy tablicy mają min. jedną cyfrę nieparzystą :)')