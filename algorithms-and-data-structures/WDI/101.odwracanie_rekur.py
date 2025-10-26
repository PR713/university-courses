
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end = '')
        head = head.next
    print('KONIEC')

def reverse(p):
    if p.next == None:
        return p, p
    rev_start, rev_end = reverse(p.next)
    #print(p.val, rev_end.val)#od końca podstawia wyżej 3 a tutaj
    #pamięta p = 5
    p.next = None #ostatni element ucina od pierwotnej
    #bez tego None na koniec będzie 5-3-2-1-2-1, bo tu 2 wskazuje na 1,
    # a 1 nadal na 2 i się zapętla 2-1-2-1....
    rev_end.next = p
    return rev_start, p

d = Node(3)
c = Node(5,d)
b = Node(2,c)
a = Node(1,b)
# 1 -> 2 -> 5 -> 3
# 3 -> 5 -> 2 -> 1

print_list(reverse(a)[0])