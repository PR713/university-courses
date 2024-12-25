class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end ='')
        head = head.next
    print("KONIEC")

def findMiddle(p):
    if p == None:
        return p

    slow, fast = p, p#jeden co jeden drugi co dwa
    #gdy fast dojdzie do None to slow będzie na środku

    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
    return slow

def merge(p1,p2):
    o = Node(None,None)
    p = o
    while p1 != None and p2 != None:
        if p1.val > p2.val:
            p.next = p2
            p2 = p2.next
        else:
            p.next = p1
            p1 = p1.next
        p = p.next

    if p1 is None and p2 is None:
        return o.next
    if p1 is None:
        p.next = p2
    else:
        p.next = p1
    return o.next

def mergeSort(p):
    if p == None or p.next == None:
        return p

    middle = findMiddle(p)
    nextmiddle = middle.next
    middle.next = None #dwie listy
    left = mergeSort(p)
    right = mergeSort(nextmiddle)
    new = merge(left,right)

    return new


i = Node(7, None)
h = Node(8, i)
g = Node(4, h)
f = Node(6, g)
e = Node(3, f)
d = Node(5, e)
c = Node(2, d)
b = Node(1, c)

print_list(b)
print_list(mergeSort(b))