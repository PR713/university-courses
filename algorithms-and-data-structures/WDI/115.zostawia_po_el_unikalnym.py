
#funkcja pozostawia w liście wyłącznie elementy unikalne.

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

def unikalne(head):
    start = head
    while head.next != None:
        p = head.next #p lecimy do przodu
        tail = head
        #head zostaje na początku i go przesuwamy
        while p != None:
            if head.val == p.val:
                tail.next = p.next #przepięcie, tail jest przed "p"
                p = p.next
            else:
                tail = tail.next
                p = p.next #p które jest na końcu przesuń dalej
        head = head.next #przesuń początek
    return start


f = Node(1)
e = Node(10,f)
d = Node(3,e)
c = Node(7,d)
b = Node(3,c)
a = Node(1,b)
g = Node(None,a)
print_list(g)
print_list(unikalne(g))
