
class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def zadB6(p):
    start = p #początek wejściowej listy
    flag1 = False
    flag2 = False
    while True:
        if p.val%2 == 0 and p.val > 0:
            if not flag1:
                even = p
                evenstart = p #początek nowej listy cyklicznej dla parzystych
                flag1 = True
            else:
                even.next = p
                even = even.next
        if p.val%2 == 1 and p.val < 0:
            if not flag2:
                odd = p
                oddstart = odd #początek dla nieparzystych
                flag2 = True
            else:
                odd.next = p
                odd = odd.next
        if p.next == start:
            even.next = evenstart
            odd.next = oddstart
            break
        p = p.next

    return evenstart, oddstart

a = Node(2)
b = Node(3)
c = Node(-5)
d = Node(8)
e = Node(-11)
f = Node(14)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = a

evenstart, oddstart = zadB6(a)
a = evenstart
while True:
    print(str(a.val) + ' -> ', end= "")
    a = a.next
    if a == evenstart:
        print('KONIEC')
        break
# 2 -> 8 -> 14 -> KONIEC
b = oddstart
while True:
    print(str(b.val) + ' -> ', end= "")
    b = b.next
    if b == oddstart:
        print('KONIEC')
        break
# -5 -> -11 -> KONIEC