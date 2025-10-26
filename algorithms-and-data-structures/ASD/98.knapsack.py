
def knapsack(W,P,B):#B - pojemność plecaka
    n = len(W)
    F = [[0 for b in range(B+1)] for i in range(n)]
    for b in range(W[0],B+1):
        F[0][b] = P[0]
    #f(i,b) maks suma cen przedmiotów ze zbioru 0,...,i
    #których waga nie przekracza b
    for b in range(B+1):
        for i in range(1,n):#próbujemy różne przedmioty dla max wagi b
            F[i][b] = F[i-1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b],F[i-1][b-W[i]] + P[i])
    return F[n-1][B]

weights = [7, 7, 1, 5, 9, 8, 7]
values = [13, 16, 1, 10, 11, 7, 10]
W = 50
print(knapsack(weights,values,W))