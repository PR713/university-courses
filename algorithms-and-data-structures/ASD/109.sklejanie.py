#Zadanie 7. (sklejanie odcinków)
#Dany jest ciąg przedziałów postaci [ai,bi]. Dwa przedziały można
#skleić jeśli mają dokładnie jeden punkt wspólny. Proszę wskazać algorytmy
#dla następujących problemów:
#1. Problem stwierdzenia, czy da się uzyskać przedział [a,b] przez
#sklejanie odcinków.
#2. Zadanie jak wyżej, ale każdy odcinek ma koszt i pytamy o minimalny
#koszt uzyskania odcinka [a,b].
#3. Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając
#najwyżej k odcinków


#a) bo b) i c) mają 150 linijek...

def binary_search_first(arr, val):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if val < arr[mid]: #[x,y] < [i,j]
            r = mid - 1
        else:
            l = mid + 1

    return r if r >= 0 and arr[r] == val else -1
    #lub l bo l == r

# Leave only intervals which can be joined to the target (begin no sooner
# than a target and end no later than a target interval)
def filter_intervals(A: 'array of intervals', target: '[a, b]'):
    A_filtered = []

    for span in A:
        if span[0] >= target[0] and span[1] <= target[1]:
            A_filtered.append(span)

    return A_filtered #bez odcinków które nas nie obchodzą
#bo wystają poza [a,b]


def intervals(A: 'array of intervals', target: '[a, b]') -> bool:
    a, b = target
    c = b - a + 1 #liczba liczb całkowitych
    F = [[None] * c for _ in range(c)]
    # Leave only intervals which can be joined to the target one
    A = filter_intervals(A, target)
    # Sort all the intervals by their first coordinate in order
    # to check quicker if an interval is in the intervals array
    A.sort() #teraz [i,j] na prawo [x,y] gdzie x >= i, y >= j
    #O(nlogn) raz po x potem po y dla par (x,y)
    def can_merge(i, j):
        # Return a cached result if exists
        # -a, -a bo wywaliliśmy przedziały wystające więc
        #przedziały jeśli jakieś są to zaczynają się od a
        #np [a,b] = [2,5], przedział [3,6] w F to [1,4]
        if F[i - a][j - a] is not None: return F[i - a][j - a]
        # Check if we have a whole [i, j] span
        if binary_search_first(A, [i, j]) >= 0:
            F[i - a][j - a] = True
            return True
        # Else look for a possible split
        F[i - a][j - a] = False
        for k in range(i + 1, j):
            F[i - a][j - a] = can_merge(i, k) and can_merge(k, j)
            if F[i - a][j - a]:
                break

        return F[i - a][j - a]

    return can_merge(a, b)