
#zaimplementować merge k posortowanych list (w sumie n elementów)

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def merge_k_linkedList(T):#T przechowuje początki linked list
    ret = Node(None)
    p = ret

    while len(T) > 1:
        mini = (0, float('inf'))
        i = 0
        while i < len(T):

            if(T[i] == None):
                T.pop(i)
                continue
            if(T[i].val < mini[1]):
                mini = (i, T[i].val)

            i += 1

        p.next = T[mini[0]]
        p = p.next
        T[mini[0]] = T[mini[0]].next

    p.next = T[0]

    return ret.next