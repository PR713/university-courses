
class Node:
    def __init__(self, index = None, next = None):
        self.next = next
        self.index = index

def print_list(head):
    print('GUARDIAN -> ', end = '')
    while head.next != None:
        print(str(head.next.index) + ' -> ', end = '')
        head = head.next
    print('KONIEC')

def remove(klucz,head):
    start = head
    while head.next != None and klucz != head.next.index:
        head = head.next

    if head.next == None:
        head.next = Node(klucz,None)
    else:#jeśli równe usuń
        head.next = head.next.next

    return start

d = Node(9)
c = Node(8,d)
b = Node(2,c)
a = Node(1,b)
g = Node(None,a)
print_list(g)
print_list(remove(8,g))
