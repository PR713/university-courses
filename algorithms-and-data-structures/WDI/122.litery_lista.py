
class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def zad33(p,string):
    first = string[0]
    last = string[-1]
    start = p
    while p.next != start:
        word1 = p.val
        word2 = p.next.val
        if word1[-1] < first and last < word2[0]:
            a = Node(string)
            a.next = p.next
            p.next = a
            return True
        p = p.next
    return False

a = Node('bartek')
b = Node('leszek')
c = Node('ola')
d = Node('zosia')

a.next = b
b.next = c
c.next = d
d.next = a
print(zad33(a,'marek'))