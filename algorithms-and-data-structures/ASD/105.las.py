#Black Forest to las rosnący na osi liczbowej gdzieś w południowej
# Anglii. Las składa się z n drzew rosnących na pozycjach
# 0, ..., n−1. Dlakażdego i ∈ {0, ..., n−1}znany jest
#zysk ci, jaki można osiągnąć ścinając drzewo z pozycji i. John
#chce uzyskać maksymalny zysk ze ścinanych drzew, ale prawo
# zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować
# algorytm, dzięki któremu John znajdzie optymalny plan wycinki.

#f(i) = max( f(i-1), f(i-2) + c(i)), i >= 2
# nie ścinamy, ścinamy f(i-2) bo nie można dwóch pod rząd
def las(c):
    n = len(c)
    val =  [0 for _ in range(n)]
    val[0] = c[0] #koszt ścięcia pierwszego drzewa
    val[1] = max(c[0],c[1]) #nie można dwóch pod rząd,
    #bierzemy max koszt z dwóch
    for i in range(2,n):#cach'eowanie
        val[i] = max(c[i]+val[i-2],val[i-1])
    return val[n-1]

