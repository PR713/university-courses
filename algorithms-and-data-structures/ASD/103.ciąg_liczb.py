#chcemy podzielić wejściowy ciąg liczb
#na 'k' części, obliczamy sumę każdej części
#najmniejsza suma ma być jak największa
#chcemy zmaksymalizować ją

#zakładki <3

def find_division(A: 'sequence of numbers to split', k: 'number of splits'):
    if k == 0: return 0

    n = len(A)
    inf = float('inf')
    F = [[0] * (k + 1) for _ in range(n)]

    # Fill the column for k = 1
    F[0][1] = A[0]
    for i in range(1, n):
        F[i][1] = F[i - 1][1] + A[i]

    # Sotore sums of values from 0 index to 'i' index
    S = [0] * n
    S[0] = A[0]
    for i in range(1, n):
        S[i] = S[i - 1] + A[i]
    #F(i,j) maksymalna wartość minimalnego ciągu kończącego się
    #na 'i' o 'j' podziałach, wynik F[n-1][k]
    # Find the maximum value of the minimum split for each k value based
    # upon results for the previous subsequences and k values
    for t in range(2, k + 1): #t podziałów
        # We will consider all numbers up to a number at 'i' index (inclusive)
        for i in range(t - 1, n): #różne miejsca podziału od t-1...n-1
        #gdzie i oznacza koniec ciągu który jest podzielony na t części
            # Loop over an index of the last number which will be included
            # in the first t - 1 splits ( indeks j)
            for j in range(t - 2, i):
                F[i][t] = max(F[i][t], min(F[j][t - 1], S[i] - S[j]))
    #czyli F(i,t) to max(F(i,t) oraz min z kończącego się na j o t-1 podziałach
    #gdzie j <= i-1, więc indeks i daje jeden podział łącznie t podziałów
    #oraz minimum z tego po prawej stronie od indeksu j+1,...,i bo albo z tej
    #albo z tej może się pojawić podział o mniejszej sumie, tzn
    #niezbędne S[i]-S[j] bo może on mieć małą sumę i by się wszystko zepsuło
    #bo chcemy to zmaksymalizować :)
    #i najpierw uzupełniamy dla t = 2 podziałów, potem dla t = 3
    #korzystamy już z podzielenia przedziału 0,...,j na 2 przedziały
    #oraz od j+1,...i jako jeden przedział więc faktycznie działa
    print(*F, sep='\n')

    return F[n - 1][k]