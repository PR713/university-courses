
def planets(D,C,T,E):
    n = len(D)
    fuel = [[float('inf') for _ in range(E+1)] for _ in range(n)]
    for i in range(E+1):
        fuel[0][i] = C[0]*i
    #f(i,j) to minimalny koszt dotarcia do planety i z j paliwa
    tp_planet = T[0][0]
    tp_price = T[0][1]
    fuel[tp_planet][0] = fuel[0][0] + tp_price
    for i in range(1,n):
        for j in range(E+1):
            dist = D[i] - D[i-1] #odległośc między planetami
            if j + dist < E: #jeżeli jest miejsce w baku
                price = fuel[i-1][dist + j]
            else: #jeżeli nie ma miejsca w baku
                price = fuel[i-1][E] + C[i]*(j + dist - E)
                #z poprzedniej z maksymalnym bakiem a nadwyżkę
                #tankujemy na następnej planecie, ok bo rozważamy wszystkie możliwości
            price2 = fuel[i][j-1] + C[i] #z poprzedniej z mniejszym bakiem o 1
            #i dodając ten jeden na 'i'tej planecie bo tamto jest minimum
            #więc tą możliwość też trzeba rozpatrzeć chcąc dolecieć z 'j'
            #jednostkami paliwa, czyli to jest sytuacja jeśli nie powinniśmy
            #tankować na 'i-1' planecie, tylko na 'i' bo tam jest taniej
            #i na niej zatankować tak żeby mieć 'j' paliwa, w tym całość na
            #planecie 'i' jeśli do tej pory cały czas price2 było minimum z tych
            #niżej albo po prostu nagle się okazało że jest to najtańsze
            #bo zatankowaliśmy za dużo na poprzedniej planecie/z inną ilością
            #wyruszono bo wcześniej price2 mogło nie być najmniejszym z tych
            #niżej bo jeszcze miało konkurenta w postaci price ale tego w if
            #a nie else: i jest tam paliwo z różnych planet wcześniej
            #a nie tylko to z else: czyli do fulla na poprzedniej :)

            fuel[i][j] = min(fuel[i][j],price,price2)
        #teleporty, j == 0
        tp_planet = T[i][0]
        tp_price = T[i][1]
        #teleport z bakiem 0, robione raz dla każdej planety 'i' już po obliczeniu wyżej
        #w pętli 'j' fuel[i][j], bierzemy minimum z już obliczonego, lub z teleportu
        fuel[tp_planet][0] = min(fuel[tp_planet][0],fuel[i][0] + tp_price)
    return min(fuel[n-1])