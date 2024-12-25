#traktor jedzie po osi liczbowej z A do B
#spalanie 1l/km, bak L litrów, A >= i >= B, i naturalne
#spotyka po drodze stacje benzynowe, i - stacje benzynowe
#a)A -> B jak najmniej tankowań
#b) c[i] = cena 1l paliwa, A->B jak najtaniej
#c) jak b) ale jeśli na stacji to do pełna tankujemy

#https://github.com/pawlowiczf/ASD-2022-2023/blob/main/Polecenia%20do%20zadań%20na%20ćwiczeniach/ASD-Cw7.pdf
def atraktor(S,L):#startujemy z pełnym bakiem dla uproszczenia
    #S tablica stacji
    result = 0
    i = 0
    while i < len(S):
        for j in range(L+i,i,-1):#jesteśmy na 'i'
            #sprawdzamy od najdalszych do najbliższych
            if j <= len(S) and S[j] == True:
                result += 1
                i = j
                break
    return result

def btraktor(K,L):#sprawdzam jaka najbliżej jest najtańsza
    n = len(K) #jeśli nie ma stacji na danej pozycji to float('inf)
    stacje = []
    pos = 0 #pusty bak na początku i nie wiemy ile w A tankować
    #więc sprawdzam pierwszy krok:
    for i in range(1,L+1):
        if K[pos] > K[i]:
            pos = i#najtańsza stacja

    while True:
        if pos + L >= n-1 and min(K[pos+1:-1]) > K[pos]:
            return stacje
            #jeśli możemy dojechać do końca and najtańsza stacja
            #do końca
        nowa_stacja = pos + 1 #potencjalna stacja
        for i in range(nowa_stacja+1,nowa_stacja+L+1):
            #szukamy najtańszej stacji 'przed' nami odległej
            #max o L, na pewno ona będzie optymalna do tankowania
            if nowa_stacja <= n-1 and K[nowa_stacja] > K[i]:
                nowa_stacja = i
        pos = nowa_stacja
        stacje.append(pos)


#if: 1)jeśli stacja na której jesteśmy jest tańsza od tych L w przód
#przed nami i nadal pos + L < n-1 to tankujemy do pełna(*) i na
#najtańszej z tych przed nami powtarzamy 1) lub 2)
#(*)a jeśli pos + L >= n-1 na tej stacji to tankujemy tyle żeby
#to co zostało tzn pos + 'coś' == n-1 (dotarliśmy optymalnie),

#else: 2)jeśli przed nami jest jakaś tańsza to jeśli dojedziemy
#na tym co mamy do niej to ok a jak nie to dotankujemy na styk
#do niej i powtarzamy 1) lub 2)

#można to zrobić już tylko przesuwając się po otrzymanej liście
#stacji 'stacje' albo w trakcie zliczać koszt




#c)
#f(i) - najniższy koszt z A do i, jeżeli tankujemy na i-tej stacji
#do pełna
#f(i) = min( f(i-L) + L*C[i], f(i-L+1) + (L-1)*C[i], f(i-1) + C[i])
#od k = 1 do L-1 min( f(i-k) + K*C[i])
#k paliwa ubyło do dojechania tu
#f(0) = 0

def ctraktor(): #dynamik, A,B mają indeksy
    return #min od k = B-L do B  f(k)