
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

def list_to_link_list(list):
    g = Node()
    for elem in list[::-1]:#gdybyśmy robili od początku to nam odwróci
        new_node = Node(elem, g.next)
        g.next = new_node
    return g

def common_part(a,b):
    p = Node()
    start = p
    while a.next != None and b.next != None:
        if a.next.val < b.next.val:
            a = a.next
        elif b.next.val < a.next.val:
            b = b.next
        else:
            r = a.next
            a.next = a.next.next #usuwamy jeden el. z listy, przeskos
            r.next = None
            p.next = r
            p = p.next
    return start


l1 = list_to_link_list([1,2,5,6,8,12,15])
l2 = list_to_link_list([1,4,5,7,12,15,20])
l3 = list_to_link_list([1,3,5,9,12,16,20])

common = common_part(l1, common_part(l2,l3))
print_list(common)
