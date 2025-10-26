
class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end ='')
        head = head.next
    print("KONIEC")

def remove_last(head):
    start = head
    if head == None:
        head.val = None
    else:
        if head.next == None:
            head.val = None
        else:
            while head.next.next != None:
                head = head.next
            head.next = head.next.next
    return start

d = Node(10)
c = Node(4,d)
b = Node(2,c)
a = Node(1,b)

print_list(a)
print_list(remove_last(a))

