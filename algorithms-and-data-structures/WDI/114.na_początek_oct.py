
#funkcja ma wskazanie na początek listy, przenosi na początek
#listy elementy które mają parzystą ilość piątek w zapisie ósemkowym

#nie trzeba sprawdzać pierwszego węzła i problem z głowy
#bo jeśli ma parzystą to już jest na przodzie, jeśli nie to
#i tak przed niego trafią poprawne
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

def sys_oct(a):
    ile_piątek = 0
    while a > 0:
        if a % 8 == 5:
            ile_piątek += 1
        a //= 8
    return ile_piątek%2 == 0


def move_oct_parz(head):
    start = head
    head = head.next
    while head != None:
        if head.next != None and sys_oct(head.next.val):
            x = head.next
            head.next = head.next.next
            x.next = start.next
            start.next = x
        else:
            head = head.next
    return start


e = Node(45) #True
d = Node(13,e) #False
c = Node(110,d) #False
b = Node(123,c) #True
a = Node(5,b) #False
g = Node(None,a)
print_list(g)
print_list(move_oct_parz(g))
