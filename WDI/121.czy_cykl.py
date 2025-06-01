
# Dana jestlista, który być może zakończona jest cyklem.
#Napisać funkcję, która sprawdza ten fakt

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def zad(p):
    if p.next == None:
        return False #czyli ma jeden el.
    slow = p
    fast = p
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

e = Node(10)
d = Node(6,e)
c = Node(7,d)
b = Node(3)#,c)
a = Node(1,b)
e.next = c #cykl c,d,e
print(zad(a))

