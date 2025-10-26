
class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end ='')
        head = head.next
    print("KONIEC")

def delete_co_2(head):
    start = head
    while head != None:
        if head.next != None:
            head.next = head.next.next
        head = head.next
    return start


f = Node(15)
e = Node(12,f)
d = Node(10,e)
c = Node(4,d)
b = Node(2,c)
a = Node(1,b)
print_list(a)
print_list(delete_co_2(a))