
#funkcja pozostawia w liście wyłącznie elementy nieunikalne.

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
    prev = head #przed head, żeby go pominąć
    head = head.next
    while head.next != None:
        p = head.next #p lecimy do przodu
        tail = head
        #head zostaje na początku i go przesuwamy
        wystapil = False
        while p != None:
            #print(p.val, head.val)
            if head.val == p.val:
                tail.next = p.next #przepięcie, tail jest przed "p"
                p = p.next
                wystapil = True
            else:
                tail = tail.next
                p = p.next
        if wystapil:
            prev.next = head.next
            head = head.next

        else:
            prev = prev.next
            head = head.next
        if head == None:
            break
    return start

h = Node(12)
g = Node(1,h)
f = Node(10,g)
e = Node(8,f)
d = Node(6,e)
c = Node(7,d)
b = Node(6,c)
a = Node(1,b)
g = Node(None,a)
print_list(g)
print_list(unikalne(g))
