class Node:
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next


def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end ='')
        head = head.next
    print("KONIEC")


def merge(p1,end1, p2, end2): #zakładam że p1, p2 to guardiany
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
        return o.next, end2 #lub end1 bo tylko gdy listy puste

    if p1.next is None:
        p.next = p2.next
        return o.next, end2
    else:
        p.next = p1.next
        return o.next, end1

def cut(p): #zakładam że p to już guardian
    q = p
    q = q.next
    if q == None: return None,None,None
    while q.next != None and q.val <= q.next.val:
        q = q.next #szukamy naturalnej serii - podciągu niemalejącego

    w = p.next #w - początek serii, q - koniec
    p.next = q.next
    q.next = None #odpinamy i mamy serię :)
    return w,q,p #p guardian - początek reszty listy
#początek serii, koniec serii, początek reszty listy

def Mergesort(head):
    tail = head
    while tail.next != None:
        tail = tail.next #tail to wskaźnik na koniec listy

    while True:
        head1, tail1, head = cut(head) #początek, koniec serii nr1 i wskazanie na resztę
        if head.next == None: return head1 #tylko gdy 1 seria
        head2, tail2, head = cut(head) #początek, koniec serii nr2 i wskazanie na resztę

        head1_g = Node(None,head1)
        head2_g = Node(None,head2)

        head_m, tail_m = merge(head1_g, tail1, head2_g, tail2)

        if head.next == None:
            break

        tail.next = head_m
        tail = tail_m
    return head_m


y = Node(6,None)
z = Node(24, y)
x = Node(0,z)
j = Node(1,x)
i = Node(7, j)
h = Node(8, i)
g = Node(4, h)
f = Node(6, g)
e = Node(3, f)
d = Node(5, e)
c = Node(2, d)
b = Node(6, c)
g = Node(None,b)

print_list(g.next)
print_list(Mergesort(g))


i = Node(36, None)
h = Node(45, i)
g = Node(31, h)
f = Node(24, g)
e = Node(29, f)
d = Node(10, e)
c = Node(2, d)
b = Node(6, c)
g = Node(None,b)

print_list(g.next)
print_list(Mergesort(g))