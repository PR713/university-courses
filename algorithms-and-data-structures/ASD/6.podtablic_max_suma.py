

def max_sum(T):
    max_suma, lewy, prawy, gorny, dolny = 0,0,0,0,0
    n = len(T[0]) #ile kolumn
    m = len(T) #ile wierszy
    for left_col in range(n):
        temp = [0] * m #przechowuje sumę w wierszach ograniczonych
        #przez kolumny lewą i prawą

        for right_col in range(left_col, n):
            suma_temp = 0
            tymczasowy_gorny = 0

            for i in range(m):
                temp[i] += T[i][right_col] #sumujemy dla kolejnych wierszy
                #kolejne kolumny wraz ze wzrostem 'i'
                suma_temp += temp[i] #dopóki nie jest ona ujemna sumujemy
                #ile wlezie a potem od indeksu 'i+1' powtarzamy

                if suma_temp > max_suma:
                    max_suma = suma_temp
                    lewy = left_col
                    prawy = right_col
                    gorny = tymczasowy_gorny
                    dolny = i

                if suma_temp < 0:
                    suma_temp = 0
                    tymczasowy_gorny = i + 1
    return max_suma, [gorny, lewy], [dolny, prawy]


T = [[100, 10],
     [20, -300],
     [0, 200],
     [0, 0]]


print(max_sum(T))