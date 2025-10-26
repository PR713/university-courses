
#Dana jest tablica T[N]. Proszę napisać program
# zliczający liczbę “enek” o określonym iloczynie.

def zad_nki(T,ilocz,nki,indeks):
    global licznik
    if nki == 1:
        for i in range(indeks,len(T)):
            if T[i] == ilocz: licznik += 1

    else:
        for i in range(indeks,len(T)):
            if ilocz%T[i] == 0: zad_nki(T, ilocz//T[i], nki-1,i+1)
            #żeby się nie powtarzały iloczyny np 2*3*5 a 5*2*3 itp

T = [1,2,5,3,5,8,2,9,5,3]
licznik = 0
zad_nki(T,24,4,0)
print("nki",licznik)
