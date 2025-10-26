def is_prime(num):
    if num > 1:
        for n in range(2,num):
            if (num % n) == 0: return False
        return True
    else:
        return False
def zad(T):
    n = len(T)
    maxi = 1
    ind = 0
    i = 0
    while i < n:
        ilo = 1
        for j in range(ind,i): #przemnażamy za każdym razem
            #wszystkie pierwsze przed indeksem 'i', a gdy już znajdziemy
            #to niżej aktualizujemy maxi i iloczyn szukamy już w przedziale
            # od ind do i-1
            if is_prime(T[j]):
                ilo*=T[j]
                print(ilo)
            if T[i] == ilo*maxi:
                if T[i] > maxi:
                    maxi = T[i]#przesuwamy iloczyn
                    ind = i#i sprawdzamy maxi* iloczyn już od indeksu ind = i
        i += 1
    return ind if ind!= 0 else None

T = [2,4,5,7,70,7,2,980,100]
print(zad(T))