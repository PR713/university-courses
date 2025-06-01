n = 5
e = [0 for _ in range(n+1)]
a = 1
s = [0 for _ in range(n+1)]
s[0] = 1
flag = True
while(flag):
    p = 0
    for i in range(n,-1,-1):
        e[i] += s[i] + p #dodajemy kolejne składniki z przesunięciem  0 lub 1
        print(e)
        p = e[i]//10 #gdy tutaj np e[i] = 10 stąd //10 = 1 do kolejnej komórki
        e[i]%=10 #dla dwucyfrowych wyników - przesuwa dopóki <10
        flag = False

    r = 0
    for i in range(0,n+1):
        print(s)
        s[i] += 10*r #obliczamy kolejne składniki (1/1) + 1/1 + 1/2+ 1/6+
        r = s[i]%a #dodajemy tak jak dla dzielenia a//b -> mod10 potem //10
        s[i]//=a#najpierw liczymy 1/2 = 0.5 potem 10//2 to 5,5.. na danym i
        if (s[i] >0):
            flag = True
    a += 1

print(e)