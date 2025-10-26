def snow(S):
    pom, sum_snow = 0, 0
    n = len(S)
    for i in range(n):
        if S[i] >= n:
            sum_snow += S[i] - pom
            S[i] = 0
            pom += 1
    #najpierw ^ sumujemy obszary >= n (bo n pól, więc te co mają
    # >= n bo to nie ma znaczenia dla wyniku)
    #i tak byśmy stracili po tych pom ( np pięciu) obszarach tyle
    #samo śniegu jeśli byśmy brali najpierw te inne obszary
    #a potem dopiero te >= n. Tyle samo się odejmie ( o ile
    #mówimy już o tych co i tak zostaną ścięte)
    #tamte na pewno trzeba ściąć, a potem po prostu po kolei
    #od największych z tych co zostały
    #no i po to żeby counting sort był dla k <= n, a nie np k = n^2
    #i żeby było O(n+k) = O(n) :)


#Te co mają ≥ n na pewno można najpierw zebrać/ściąć (bo n pól śniegu),
#no i dla >= n jeśli wiele jest >= n to bez problemu, jeśli zaś jedno i to równe 'n'
#to zostanie ono jako ostatnie ze śniegiem równym 1 (bo można np 50 - 1 + 40 - 2 ale
#też 50 - 2 + 40 - 1), np >= n-1 już nie działa bo mogłoby się wyzerować a niepotrzebnie
#go zliczamy tracąc na tym zbiory np 2,3,3 -> 1 + 2 + 1 = 4 lub 3 + 2 = 5, i teoretycznie by
#to działało o ile i tak by były uporządkowane pola że najpierw by były te >= n
# xD...

#zawsze od największych na chwilę obecną zbieramy i to jest poprawne :) (bo daje nam
#to największe możliwości np po co zbierać mając 1, 10, 10 -> 1 + 9 + 8 => 18 (3 zbiory)
#jak można w dwóch zbiorach, o jeden do przodu bo 10 + 9 = 19 i tej jeden zbiór powoduje
#że strata o 1 jest

#dlatego jedynki są czasem problematyczne... sama ilość zbiorów i tyle np 3,10,10,10
#-> 2 + 9 + 8 + 7 = 26 != 10 + 9 + 8 = 27, jedynki nie mają jako tako znacznia, kluczowe
#są zbiory od największych wartości bo daje największe możliwości niż każde inne podejście


#również nie można np ≥ n-3 bo najpierw weźmie dające mniej zysku np 1,2,4,10,10,10
#mimo że najpierw się powinno od największych, widać to np dla
#1, 2, 3, 10, 11, 12 jeśli chodzi o największe
    max_el = 0
    for i in range(n):
        if S[i] > max_el:
            max_el = S[i] #szukamy zakresu 0,..., k - 1
    k = max_el + 1
    B = [0]*n
    C = [0]*k
    for x in S:
        C[x] += 1
    for i in range(1,k): C[i] += C[i-1]
    for i in range(n-1,-1,-1):
        B[C[S[i]] - 1] = S[i]
    for i in range(n):
        S[i] = B[i]
    #mamy posortowaną listę S

    index = n - 1
    while S[index] - pom > 0 and index >= 0:
        sum_snow += S[index] - pom
        pom += 1
        index -= 1

    return sum_snow

A = [4,20,6,3,2,1]
B = [60,40,100,2,50]
print(snow(A))
print(snow(B))


