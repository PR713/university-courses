#Przyczepa ma pojemność K kg, zbiór ładunków
#o wagach w1,...,wn: dla każdego i istnieje k naturalne
# w_i = 2^k, czyli wagi to potęgi dwójki, Wybrać ładunki tak,
#by max. zapełnić przyczepą a ładunków było min.
#liczby binarne kolejne potęgi 2
#bierzemy najcięższe aż się wypełni
#bo np K = 33
#wagi 2,2,4,8,16,32 i jeśli dałoby się wypełnić do i tak
#się uda

def load(K,W):
    W.sort() #nlogn
    res = []
    i = len(W)-1
    while i != 0:
        if W[i] <= K:
            K -= W[i]
            res.append(W[i])
        i -= 1
    return res

