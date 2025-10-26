def is_correct(x):
    count = 0
    i = 2
    while x > 1:
        if x % i == 0:
            count += 1
            if count > 2:
                return False
            else:
                while x % i == 0:
                    x //= i
        i += 1
    if count == 2:
        return True
    return False

def square(T):
    n = len(T)
    for a in range(2,n):
        for i in range(n-a+1):
            for j in range(n-a+1):
                if is_correct(T[i,j]*T[i+a-1,j]*T[i,j+a-1]*T[i+a-1][j+a-1]):
                    return a
    return 0
