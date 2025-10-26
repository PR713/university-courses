#wybierając spośród nich minimum i przestawiając je do
#drugiej nowej list, przez to obecna lista staje się
# o 1 krótsza i zaczynamy znowu od początku tworząc w drugiej
#liście ciąg rosnący

class Node:
    def __init__(self):
        self.val = None # przechowywana liczba rzeczywista
        self.next = None # odsyłacz do nastepnego elementu

#def print_list(head):
#    while head != None:
#        print(str(head.val) + ' -> ', end ='')
#        head = head.next
#    print("KONIEC")

def sortH(p, k):
    g1 = Node()
    g1.next = p
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
                #print('siema')

            if p.next != None: #to mimo wszystko przesuwamy dalej,
                #w przeciwnym wypadku na początek na końcu while
                p = p.next
                prev = prev.next
            else: break

        if g1.next == mini: #to usuwamy pierwszy
            g1.next = q.next
            end2.next = q
            end2 = end2.next
            q.next = None #OKKKK
            #####print_list(g1) #########

        else: #usuwamy środek
            q.next = mini.next
            mini.next = None
            end2.next = mini
            end2 = end2.next
            #####print_list(g1) ########

        #po zakończeniu fora i reszty pora wrócić z prev i p
        prev = g1.next
        p = prev.next

    end2.next = g1.next

    return g2.next

#p,c,d,e,f,g,h = Node(), Node(),Node(),Node(),Node(),Node(),Node()
#p.val, c.val, d.val, e.val, f.val, g.val, h.val = 1,0,3,2,4,6,5
#p.next, c.next, d.next, e.next, f.next, g.next, h.next = c,d,e,f,g,h, None
#print_list(p)
#print_list(sortH(p,1))