
def zad13(n):
    T = [0]*n
    def rek(n,i,T):
        if n == 0:
            print(T)
        if i == 0:
            mini = 1
        else:
            mini = T[i-1] #czyli bierzemy ostatnio wpisaną
        for j in range(mini,n+1):
            T[i] = j
            rek(n-j,i+1,T)
            T[i] = 0
    rek(n,0,T)

zad13(4)






#lub
"""
def ile_cyfr(i):
    cnt = 0
    while i > 0:
        i //= 10
        cnt +=1
    return cnt

def rek(s,min = 1, z="", x=40):
    if s == x:
        print(z)
        return
    if s > x:
        return
    if s != 0:
        z += "+"
    for i in range(min,x):
        s+=i
        z+= str(i)
        rek(s,i,z,x)
        s-=i
        n = len(z)

        cnt = ile_cyfr(i)
        z = z[0:n-cnt]#ucinamy to i które dodaliśmy wyżej
        #dla wielocyfrowych żeby sie nie psuło trzeba już ucinać
        #więcej cyfr dlatego n - cnt
"""
#rek(0,min = 1, z="")
