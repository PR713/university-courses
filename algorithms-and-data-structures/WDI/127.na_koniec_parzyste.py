
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end='')
        head = head.next
    print('KONIEC')



def repair(p):
    g = Node(None,p)
    prev = g
    parz = Node()

    while p != None:
        if p.val % 2 == 0:
            prev.next = p.next
            p.next = parz.next
            parz.next = p
            p = prev.next
        else:
            prev = prev.next
            p = p.next
    prev.next = parz.next
    return g.next

e = Node(8)
d = Node(2,e)
c = Node(7,d)
b = Node(6,c)
a = Node(1,b)

print_list(a)
print_list(repair(a))



