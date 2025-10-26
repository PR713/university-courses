#A - n elementowa tablica
#znaleźć x,y z A takie, że y-x jest największe i nie ma
#z takiego że x < z < y
#szukamy min_A i max_A
#zakres od min_A,..., max_A
# 1) jak w każdym  jest jeden element to już mamy posortowane
# i bierzemy z jednego kubełka max a z następnego kubełka min
# 2) lub co najmniej 1 pusty to z poprzedniego od pustego bierzemy
# max a z następnego po nim niepustego minimum
#zawsze pierwszy i ostatni kubełek zawierają element, sąsiedzi niepuści
#odpowiednio minimum_A i maximum_A