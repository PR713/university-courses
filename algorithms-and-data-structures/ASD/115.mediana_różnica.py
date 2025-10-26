#Dana posortowana A[n] rzeczywiste
#Znaleźć x które nie musi być w A że : suma od i = 0 do n-1 po |A[i]-x|
# jest minimalne
#szukane x to mediana, środkowa dla n = 2k + 1,
#a dla parzystych mediana to średnia, a szukany x to dowolna liczba
#pomiędzy tymi medianami dla n parzystego czyli z przedziału
#( A[n//2 - 1], A[n//2] )
# Dowód:
#Gdy x jest mniejsze niż mediana, zwiększenie x o małą wartość
#zmniejszy różnice dla wartości większych niż mediana bardziej
#niż zwiększy różnice dla wartości mniejszych niż mediana
#co ogólnie zmniejszy sumę wartości bezwzględnych.

#Gdy x jest większe niż mediana, zmniejszenie x o małą wartość
#zmniejszy różnice dla wartości mniejszych niż mediana bardziej
#niż zwiększy różnice dla wartości większych niż mediana.
def median(A):
    n = len(A)
    count = [0]*(max(A)+1)
    if n % 2 == 0:
        return (A[n//2 - 1] + A[n//2])/2
    else: return A[n//2] #nieparzysta ilość n = 2k+1

