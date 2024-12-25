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

def merge(left,right):
    if left == None:
        return right
    if right == None:
        return left
    new = None
    if left.val <= right.val:
        new = left
        new.next = merge(left.next,right)
    else:
        new = right
        new.next = merge(left,right.next)

    return new

def mergeSort(p):
    if p == None or p.next == None:
        return p

    middle = findMiddle(p)
    nextmiddle = middle.next
    middle.next = None #dwie listy
    left = mergeSort(p)
    right = mergeSort(nextmiddle)
    new = merge(left,right) #wywołuje merge na każdym poziomie
    #które wykona się gdy już skończą się wywołania left i right
    return new #lub return merge(left,right)


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