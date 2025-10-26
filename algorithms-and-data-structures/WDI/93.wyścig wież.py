
def wzgl_pierw(a,b):
    while a != 0:
        a,b = b%a, a
    return b == 1

def rook_race(T):
    rook1_time = float('inf')
    rook2_time = float('inf')
    def rook1_rec(r=0,c=0,cnt=0):
        n = len(T)
        nonlocal rook1_time
        if r == c == n-1:
            if cnt < rook1_time:
                rook1_time = cnt
        else:
            for i in range(r+1,n):
                if wzgl_pierw(T[r][c],T[i][c]):
                    rook1_rec(i,c,cnt+1)
            for i in range(c+1,n):
                if wzgl_pierw(T[r][c],T[r][i]):
                    rook1_rec(r,i,cnt+1)

    def rook2_rec(r=0,c=len(T)-1,cnt=0):
        n = len(T)
        nonlocal rook2_time
        if r == n-1 and c == 0:
            if cnt < rook2_time:
                rook2_time = cnt
        else:
            for i in range(r+1,n):
                if wzgl_pierw(T[r][c],T[i][c]):
                    rook2_rec(i,c,cnt+1)
            for i in range(0,c):
                if wzgl_pierw(T[r][c],T[r][i]):
                    rook2_rec(r,i,cnt+1)
    rook1_rec()
    rook2_rec()
    if rook1_time == rook2_time:
        return 0
    elif rook1_time < rook2_time:
        return 1
    return 2


