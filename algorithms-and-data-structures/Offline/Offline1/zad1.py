#Radosław Szepielak
#Rozważam wielkość k względem n - długości listy jednokierunkowej i na podstawie tego,
#wybieram jedno z dwóch rozwiązań. Pierwsze sortowanie polega na znajdowaniu za każdym
#razem wśród k+1 pierwszych elementów listy minimum, któro przepinamy do nowej listy (k+1 ponieważ
#bieżemy pierwszy element i rozważamy k kolejnych elementów po nim następujących). W ten sposób
#utworzymy już posortowaną listę, ponieważ każdy element po posortowaniu byłby na pozycji różniącej
#się od pierwotnej o najwyżej k, zatem zawsze wśród k+1 pierwszych elementów jakie zostaną
#w pierwotnej link liście znajdzie się minimum, któro będzie następnym elementem w posortowanej
#liście. Drugie sortowanie natomiast jest sortowaniem MergeSort, który dzieli link listę
#rekurencyjnie na połowy, a następnie te połówki sortuje iteracyjnie w coraz większe link
#listy wraz z rekurencją. Znajdywanie środka podziału odbywa się w taki sposób, że jeśli
#wskaźnik przemieszczający co dwa elementy dotrze do końca link listy, to wskaźnik
#wolniejszy przesuwający się co jeden element wyznaczy nam środek.
#Finalnie otrzymujemy posortowaną link listę.
#
#Złożoność czasowa danego programu:
#- dla k = Θ(1) jest to złożoność czasowa O(n)
#- dla k = Θ(log n) jest to złożoność czasowa O(n*log(n))
#- dla k = Θ(n) jest to złożoność czasowa O(n*log(n))

from zad1testy import Node, runtests


def SortH(p,k):
    if k == 0:  # czyli 0-chaotyczna, już posortowana
        return p
    cnt = 1  # link lista niepusta
    x = p.next
    flag = False  # jeśli True wybiera pierwsze sortowanie, False - drugie
    v = 2 ** k
    while x != None:#rozważam k względem aktualnie zmierzonej długości link listy - cnt
        cnt += 1 #nie musi być cnt = n żeby stwierdzić poniższe
        if v < cnt:  # 2**k < cnt -> k < log_2 (cnt)
            flag = True  # ponieważ pierwsze sort. O(n*k), drugie O(n*log(n)) to jest to optymalne
            break
        x = x.next

    if flag:
        g1 = Node() #wartownik do pierwotnej link listy
        g1.next = p
        g2 = Node() #wartownik do posortowanej link listy
        end2 = g2  #end2 wskaźnik na koniec posortowanej link listy
        prev = p  #wskaźnik przed p
        p = p.next

        while p != None:
            minival = prev.val
            mini = prev
            q = prev
            for _ in range(k):
                if p.val < minival:  # znajdywanie minimum
                    q = prev
                    mini = p
                    minival = p.val

                if p.next != None:
                    p = p.next
                    prev = prev.next
                else:
                    break

            if g1.next == mini:  # jeśli minimum to pierwszy element po wartowniku
                g1.next = q.next
                end2.next = q
                end2 = end2.next
                q.next = None
            else:  # reszta przypadków
                q.next = mini.next
                mini.next = None
                end2.next = mini
                end2 = end2.next

            prev = g1.next
            p = prev.next

        end2.next = g1.next  # dopinam ostatni element z pierwotnej listy
        g1.next = None
        return g2.next
    else:
        def findMid(a):  # szukanie środka podziału na dwie tablice
            if a == None:
                return a

            slow, fast = a, a

            while fast.next != None and fast.next.next != None:
                fast = fast.next.next  # wskaźnik szybki co dwa elementy
                slow = slow.next  # wolny co jeden element
            return slow  # znaleziony środek

        def merge(p1, p2):
            o = Node()
            b = o
            while p1 != None and p2 != None:  # łączę dwie link listy (połówki) dopóki któraś nie stanie się pusta
                if p1.val > p2.val:
                    b.next = p2
                    p2 = p2.next
                else: #jeśli zachodzi '<=' to bierzemy z lewej listy, stabilne sortowanie
                    b.next = p1
                    p1 = p1.next
                b = b.next

            if p1 is None and p2 is None:
                return o.next
            if p1 is None:
                b.next = p2
            else:
                b.next = p1
            return o.next

        def mergeSort(h):
            if h == None or h.next == None:
                return h

            half = findMid(h)
            next_middle = half.next
            half.next = None
            left = mergeSort(h)  # rekurencyjne wywołanie do posortowania lewej połówki listy
            right = mergeSort(next_middle)  # rekurencyjne wywołanie do posortowania prawej połówki
            new = merge(left, right)  # scala posortowane lewe i prawe połowy

            return new

        return mergeSort(p)
    pass

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
