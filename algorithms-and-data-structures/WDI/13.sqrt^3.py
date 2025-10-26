S = float(input('Pierwiastek 3 stopnia z: '))
a = 0
k = 1
eps = 1e-10
while abs(k - a) > eps:
    a = k
    k = (S /(a*a) + 2*a)/3
    #print(k)
print(k)
