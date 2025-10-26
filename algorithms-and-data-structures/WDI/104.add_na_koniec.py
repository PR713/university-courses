
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


def add(head,val):
    start = head
    while head.next != None:
        head = head.next
    head.next = Node(val)
    return start

c = Node(4)
b = Node(2,c)
a = Node(1,b)
g = Node(None,a)

print_list(g)
print_list(add(g,10))