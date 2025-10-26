
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

def del_(head):#jeśli następny ma val < od poprzedniego to ma go usunąć
    start = head # 5 -> 3 -> 4 -> 7  powstanie 5 -> 7
    head = head.next
    while head != None and head.next != None:
        if head.val > head.next.val:
            head.next = head.next.next
        else:
            head = head.next

    return start

e = Node(10)
d = Node(14,e)
c = Node(2,d)
b = Node(3,c)
a = Node(5,b)
g = Node(None,a)
print_list(g)
print_list(del_(g))
