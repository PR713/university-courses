
#Scalanie dwóch posortowanych list jednokierunkowych do jednej

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end ='')
        head = head.next
    print("KONIEC")

def merge(p1,p2): #zakładamy p1, p2 guardiany
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
        return o #tylko gdy obie listy puste na wejściu

    if p1.next is None:
        p.next = p2.next
    else:
        p.next = p1.next
    return o.next

c = Node(6)
b = Node(4, c)
a = Node(1, b)
p1 = Node(None,a)

c1 = Node(8)
b1 = Node(4, c1)
a1 = Node(3, b1)
p2 = Node(None,a1)

print_list(a)
print_list(a1)
print_list(merge(p1,p2))

