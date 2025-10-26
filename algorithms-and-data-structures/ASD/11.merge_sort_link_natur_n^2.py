#TAAAAAAAAK
#Algorytm sortowania list jednokiernkowych przez scalanie serii naturalnych
# (1 -> 2 -> 5) -> (3 -> 6) -> (4 -> 8) -> (7)

#trzeba co chwilę merge'ować, odcinami po
#serii, jak się skończy to potem odcinanie kolejnych
#trzeba merge z tymi już w nowej liście

class Node:
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next


def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end ='')
        head = head.next
    print("KONIEC")


def merge(p1,p2): #zakładam że p1, p2 to guardiany
    o = Node()
    p = o
    while p1.next != None and p2.next != None:
        if p1.next.val > p2.next.val:
            p.next = p2.next
            p = p.next
            p2.next = p2.next.next
        else:
            p.next = p1.next
            p = p.next
            p1.next = p1.next.next

    if p1.next is None and p2.next is None:
        return o

    if p1.next is None:
        p.next = p2.next
    else:
        p.next = p1.next
    return o

def cut(p): #zakładam że p to już guardian
    q = p
    q = q.next
    if q == None: return None,None
    while q.next != None and q.val < q.next.val:
        q = q.next #szukamy naturalnej serii - podciągu niemalejącego

    w = p.next #w - początek serii, q - koniec
    p.next = q.next
    q.next = None #odpinamy i mamy serię :)
    return w,p #p guardian - początek reszty listy


def Mergesort(head):
    new = Node()
    while head != None:
        a, head = cut(head)
        aguard = Node(None,a) #guardian odcinanej serii
        if a != None: #lub head, czy lista pierwotna coś jeszcze ma
            new = merge(new, aguard)
        else:
            break
    return new.next


i = Node(7,None)
h = Node(8, i)
g = Node(4, h)
f = Node(6,g)
e = Node(3,f)
d = Node(5, e)
c = Node(2, d)
b = Node(1, c)
g = Node(None,b)

print_list(g.next)
print_list(Mergesort(g))



