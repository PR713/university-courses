
#funkcja usuwająca wszystkie elementy, których wartość dzieli
#bez reszty wartość bezpośrednio następujących po nich elementów.


class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def print_list(head):
    print("GUARDIAN -> ", end = '')
    while head.next != None:
        print(str(head.next.val) + ' -> ', end ='')
        head = head.next
    print("KONIEC")

def delete(head):#jeśli wartośc elementu dzieli bez reszty
    #next.val to ma go usunąć ten pierwszy
    start = head
    prev = head
    head = head.next
    while head != None and head.next != None:
        if head.next.val % head.val == 0:
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next
    return start

e = Node(10)
d = Node(8,e)
c = Node(4,d)
b = Node(5,c)
a = Node(2,b)
g = Node(None,a)
print_list(g)
print_list(delete(g))
