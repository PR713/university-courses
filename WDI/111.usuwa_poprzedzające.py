
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

def del_(head):#jeśli val elementu jest < od val.next to ma usunąć obecny
    start = head
    prev = head
    p = head.next #lub zamiast tego head = head.next i operować na head
    while p != None and p.next != None:
        if p.val < p.next.val:
            prev.next = p.next
        else:
            prev = prev.next #jeśli val nie jest < to prev trzeba przesunąć
        p = p.next

    return start
#bez guardiana chyba lepiej bo na początku tworzymy pustego Node
e = Node(10)
d = Node(7,e)
c = Node(3,d)
b = Node(20,c)
a = Node(1,b)
g = Node(None,a)
print_list(g)
print_list(del_(g))
