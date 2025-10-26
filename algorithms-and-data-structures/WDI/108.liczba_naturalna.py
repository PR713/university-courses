
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


def zad9(head): #zwiększanie o "1" liczbę
    start = head
    flag = False
    def liczba_naturalna(head):
        nonlocal flag
        if head.next != None:
            liczba_naturalna(head.next)

        if head.val == 9 and flag != True: #jeśli ostatni to 9 i flaga False
            #czyli nie dodano jeszcze to zeruj i rekurencyjnie potem
            #jak znajdzie < 9, czyli się skończą 9 od końca to wrzuci tam +1
            # np z 1999 -> 2000
            head.val = 0
        elif head.val < 9 and flag != True:
            head.val += 1
            flag = True

        return start
    liczba_naturalna(head.next)
    #jeśli nadal False czyli liczba to np 999 więc w wartowniku trzeba
    #zrobić value z 0 na 1.
    if flag == False:
        start.val += 1
    return start

d = Node(9)
c = Node(9,d)
b = Node(2,c)
a = Node(1,b)
g = Node(0,a)
print_list(g)
print_list(zad9(g))