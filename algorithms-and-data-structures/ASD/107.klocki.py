#Zadanie 2. (spadająceklocki)
#Każdy klocek to przedział postaci [a, b]. Dany jest ciąg
#klocków [a1, b1], [a2, b2], ..., [an, bn].
#Klocki spadają na oś liczbową w kolejności podanej w ciągu.
#Proszę zaproponować algorytm, który oblicza, ile klocków należy
#usunąć z listy tak, żeby każdy kolejny spadający klocek mieścił
#się w całości w tym, który spadł tuż przed nim


#f(i) - wysokość najwyższej wieży, gdy klocek
#'i' znajduje się na górze
#f(i) = max(f(j)+1) po wszystkich j takich że klocek
#'i' może być położony na klocku 'j'

def klocki(T):
    n = len(T)
    F = [1 for _ in range(n)]
    for i in range(1,n): #dla kolejnych klocków
        a,b = T[i]
        for j in range(i):#czy 'i' można położyć na poprzednim 'j'
            c,d = T[j]
            if c <= a and d >= b: #klocek 'i' na 'j'
                F[i] = max(F[i], F[j] + 1)
    max_height = max(F)
    wynik = n - max_height #tyle do usunięcia
    return wynik
