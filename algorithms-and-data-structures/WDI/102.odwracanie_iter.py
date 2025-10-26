
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end='')
        head = head.next
    print('KONIEC')

def odwracanie(p):
    o = Node()
    while p != None:
        q = p.next
        p.next = o.next #czyli na początku p.next = None
        o.next = p
        p = q
    return o.next

e = Node(3)
d = Node(7,e)
c = Node(4,d)
b = Node(2,c)
a = Node(1,b)
print_list(odwracanie(a))