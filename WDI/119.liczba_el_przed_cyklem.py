
class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def zad(p):
    slow = p
    fast = p
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = p
    cnt = 0
    while slow != fast:
        slow = slow.next
        fast = fast.next
        cnt += 1

    return cnt




e = Node(10)
d = Node(6,e)
c = Node(7,d)
b = Node(3,c)
a = Node(1,b)
e.next = c #cykl c,d,e
print(zad(a))

