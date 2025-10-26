
#sortowanie przez wybór

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end ='')
        head = head.next
    print("KONIEC")

def sort(p):
    x = Node()
    while p != None:
        mini = Node()
        mini.next = p
        pom = p
        while pom.next != None:
            if pom.next.val < mini.next.val:
                mini = pom
            pom = pom.next #pom leci do końca, mini to poprzednik minimum
            # nowo znalezionego
        if mini.next == p:#jeśli mini nie uległo zmianie to przesuń p
            p = p.next
        y = mini.next
        mini.next = mini.next.next #lub y.next
        y.next = x
        x = y #x początek nowej list przesuwa się w lewo
    return x


head = Node(3)
head.next = Node(1)
head.next.next = Node(5)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)
print_list(head)
print_list(sort(head))



