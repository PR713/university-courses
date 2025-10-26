def Fib(a,b):
    while a < 1000000: # lub np a < 1000
        c = a +b
        a = b
        b = c # 1,1,2,3,5,8
        #x = a+b # = c w kolejnej
        #print(a,b,a+b) # to a,b,c
        #print((a+b)/b, b/a) # wyraz następny, poprzedni
        if abs(b/a - (a+b)/b) < eps: #KUR*a trzeba ABS
            #print(a,b)
            return (a+b)/b

eps = 1e-5
a = 1
b = 1
print(f'Ciag Fibonacciego zmierza do liczby φ : {Fib(a,b)} ')