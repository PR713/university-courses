class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def print_list(head):
    print('GUARDIAN -> ', end='')
    while head.next != None:
        print(str(head.next.val) + ' -> ', end='')
        head = head.next
    print('KONIEC')


def remove_element(p, to_delete):
    start = p
    while p.next != None:
        if p.next.val == to_delete:
            p.next = p.next.next
            return start
        p = p.next

    return start


def add_element(p, to_add):#na końcu
    start = p
    while p.next != None:
        p = p.next

    p.next = Node(to_add)
    return start


c = Node(3)
b = Node(2, c)
a = Node(1, b)
g = Node(None, a)

print_list(g)
g = add_element(g, 4)
print_list(g)
g = remove_element(g, 5)
print_list(g)