
#idea: Sortujemy za każdym razem pierwsze k elementów
#wybierając spośród nich minimum i przestawiając je do
#drugiej nowej list, przez to obecna lista staje się
# o 1 krótsza i zaczynamy znowu od początku tworząc w drugiej
#liście ciąg rosnący

class Node:
    def __init__(self, val = None, next = None):
        self.val = val # przechowywana liczba rzeczywista
        self.next = next # odsyłacz do nastepnego elementu

def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end ='')
        head = head.next
    print("KONIEC")

def sortH(p, k):
    g1 = Node(None,p)
    g2 = Node()
    end2 = g2 #będzie końcem drugiej listy
    prev = p
    p = p.next # p następny po prev

    if k == 0: return g1.next

    while p != None:
        minival = prev.val
        mini = prev
        q = prev #gdyby if niżej nigdy nie wykonał się
        for _ in range(k):
            if p.val < minival:
                q = prev #wskaźnik przed mini
                mini = p #wskaźnik na mini
                minival = p.val

            if p.next != None: #to mimo wszystko przesuwamy dalej,
                #w przeciwnym wypadku na początek na końcu while
                p = p.next
                prev = prev.next
            else: break

        if g1.next == mini: #to usuwamy pierwszy
            g1.next = q.next
            end2.next = q
            end2 = end2.next
            q.next = None #OKKK
        else: #usuwamy środek
            q.next = mini.next
            mini.next = None
            end2.next = mini
            end2 = end2.next

        #po zakończeniu fora i reszty pora wrócić z prev i p
        prev = g1.next
        p = prev.next

    end2.next = g1.next

    return g2.next

h = Node(5, None)
g = Node(6, h)
f = Node(4,g)
e = Node(2,f)
d = Node(3, e)
c = Node(0, d)
p = Node(1, c)
print_list(p)
print_list(sortH(p,1))