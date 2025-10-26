#N - el. tablica T liczb wymiernych
#dane powstały z rozkładu:
#k - przedziałów [a1,b1), [a2,b2)...[ak, bk)
#takie że i-ty przedział wybierany jest z prawdopodobieństwem
#c_i, ai, bi {0,...,N-1}
# jak 1 kopiec nie wystarczy to 2 kopce,
# jak więcej to sortowanie kubełkowe
#sortujemy do N kubełków i w danym kubełku znowu sortujemy kubełkowo
#trzeba zliczyć ile jest elementów w kubełku i tyle w nim kubełków
#będzie ich max 2k