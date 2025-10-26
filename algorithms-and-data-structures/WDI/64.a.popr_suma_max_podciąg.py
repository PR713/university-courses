def max_podciag(T):
    n = len(T)
    sum_max = 0
    for i in range(n):
        for j in range(n):
            sum1 = T[i][j]
            sum2 = T[i][j]
            for k in range(1, 11):
                if i + k >= n: break
                sum1 += T[i + k][j]
                sum_max = max(sum1,sum_max)
            for k in range(1, 11):
                if j + k >= n: break
                sum2 += T[i][j + k]
                sum_max = max(sum2,sum_max)
    return sum_max

tab = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
print(max_podciag(tab))
