import random
def prob(n):
    year = [-1 for _ in range(366)]
    counter = 0
    ile_prob = 1000
    for i in range(ile_prob):    #ilosc prób
        for j in range(n):  #ilosc osob (20-40)
            birthday = random.randint(1, 365)
            if year[birthday] == i:#sprawdzamy na 10000 prób losując dla 20-40 osób dopóki się dzień powtórzy
                counter += 1 #bo szukamy do póki znajdziemy albo nie znajdziemy, prawdopodobieństwo 1/2
                break
            year[birthday] = i
    return counter/ile_prob

print(prob(26))