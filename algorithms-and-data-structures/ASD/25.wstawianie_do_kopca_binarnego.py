
#zaimplementować wstawianie do kopca binarnego

def parent(i): return (i-1)//2

def heap_insert(t,val):
    n = len(t)
    t.append(val)
    i = n
    p = parent(i)
    while i > 0 and t[p] < t[i]:
        t[p], t[i] = t[i], t[p]
        i = p
        p = parent(i)

heap = []
heap_insert(heap,1)
heap_insert(heap,2)
heap_insert(heap,1.5)
heap_insert(heap,88)
print(heap)