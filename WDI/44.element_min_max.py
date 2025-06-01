tab = [3,7,2,4,19,15,13,11,10,2,7,9,20,21,1,27]

def maxmin(tab):
    min, max = tab[0], tab[0]
    for i in range(0,len(tab)):
        if tab[i] < min:
            min = tab[i]
        if tab[i] > max:
            max = tab[i]

    cnt1, cnt2 = 0, 0
    for i in range(0,len(tab)):
        if tab[i] == min:
            cnt1 += 1
        if tab[i] == max:
            cnt2 += 1
    if cnt1 == 1 and cnt2 == 1:
        return True
    return False

print(maxmin(tab))
