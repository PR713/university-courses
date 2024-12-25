#Zadanie 4. (Głodna żaba)
# Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n−1,
#skacząc wyłącznie w kierunku większych liczb.
 #Skok z liczby i do liczby j (j>i) kosztuje ją j−i jednostek
 #energii, a jej energia nigdy nie może spaść poniżej zera.
#Napoczątku żaba ma 0 jednostek energii, ale na szczęście
 #na niektórych liczbach– także na zerze– leżą przekąski
 #o określonej wartości energetycznej (wartość przekąski dodaje się
 #do aktualnej energii żaby). Proszę zaproponować algorytm, który
 #oblicza minimalną liczbę skoków potrzebną na dotarcie
 #z 0do n−1, mając daną tablicę A z wartościami energetycznymi
 #przekąsek na każdej z liczb

def zaba(A):#F(i,j) z energią 'i' na polu 'j'
    n = len(A)
    F = [[float('inf')] * n for _ in range(n)]

    # Fill the first column with zeros (no jumps required to get to the starting
    # point as we are already there)
    for i in range(n):
        F[i][0] = 0

    # Set number of jumps required to get to the 'i'th field having still 'A[0] - i'
    # energy remaining with ones (one jump required). This is essential step as we
    # can go only tho these fields from the beginning one.
    for i in range(A[0]):
        F[i][A[0] - i] = 1

    # Fill the remaining fields of an array with appropriate values (minimum
    # number of steps required to get to such a field with the certain amount of
    # energy remaining).
    for i in range(n): #w tablicy dla różnych od najmniejszych energii
    #bo robiąc od (n-1,-1,-1) pominęlibyśmy możliwe w przyszłości
    #większe energie, a tutaj już mniejsze nas nie będą obchodziły
        for j in range(1, n):#dojście na pole 'j'
            if F[i][j] < float('inf'):
                energy = min(A[j] + i, n - 1 - j)
                #minimum z tego ile energii mamy docierając tu
                #z energią 'i' + przekąska A[j]
                #i ograniczenie żeby nie wylecieć poza tablicę
                # k is the remaining energy
                for k in range(energy):
                    # Limit an energy to the max value essential to reach the end
                    # (This step is required in order not to go out of the bounds
                    # of the F matrix (and to limit the memory required to cache values))
                    next_j = j + energy - k
                    # Store the minimum steps required to get to the 'next_j' index
                    F[k][next_j] = min(F[k][next_j], F[i][j] + 1)

    print(*F, sep='\n')
    return F[0][n - 1]

A = [2, 3, 1, 1, 2, 0]
print(zaba(A))
A = [2, 2, 1, 0, 0, 0]
print(zaba(A))