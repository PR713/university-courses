
def counting_sort(T,index):
    n = len(T)
    B = [0]*n
    C = [0]*26

    for x in T:
        if index >= len(str(x)):
            C[0] += 1 #jako dopełniamy literami 'a'
        else:
            C[ord(x[index]) -97] += 1

    for i in range(1,26):
        C[i] += C[i-1]

    for i in range(n-1,-1,-1):
        if index >= len(str(T[i])):
            B[C[0] - 1] = T[i]
            C[0] -= 1
        else:
            B[C[ord(T[i][index])-97]-1] = T[i]
            C[ord(T[i][index]) - 97] -= 1
    return B

def radix_sort(T):
    for i in range(25,-1,-1):
        T = counting_sort(T,i)
    return T


T = ["tygrys","kot","wilk","trysyg","wlik","sygryt","likw","tygrys"]
print(radix_sort(T))