#Zadanie 4. (wieże) Grupa m dzieci bawi się w układanie możliwie jak największej wieży. Każde dziecko
#ma klocki różnej wysokości. Pierwsze dziecko ma klocki o wysokościach
#w1-1,...,w1-n1
#drugie dziecko klocki o wyskościach w2-1,...,w2-n2 itd. Dzieci właśnie
#poszły zjeść deser zanim ułożą swoje wieże, ale jedno dziecko
#zostało. Ma teraz jedyną okazję, żeby podebrać kilka klocków innym dzieciom
#tak, żeby jego wieża była najwyższa. Proszę podać możliwie najszybszy
#algorytm rozwiązujący ten problem, który zabiera minimalną ilość klocków.
#(Proszę zwrócić uwagę, że liczby wi-j mogą być bardzo duże.)

#złodziej > T wysokość
# i  <= T, T jest wielomianowo dużo
#najpierw dzieciom zabieramy klocki żeby im obniżyć
#potem sobie zwiekszamy żeby już przekroczyć
#suma długości klocków dla każdego z dzieci to brute trochę

###################################
class MaxHeap:
    def __init__(self, values=None):
        if values:
            self.heap = values
            self.build_heap()
        else:
            self.heap = []

    def __bool__(self):
        return bool(self.heap)

    def __gt__(self, other):  # This is only to enable heap comparisons
        if isinstance(other, self.__class__):
            if not other: return bool(self)
            if not self:  return bool(other)
            return self.get_max() > other.get_max()
        return bool(other) if not self else self.get_max() > other

    def __ge__(self, other):
        return (self < other or self.get_max() == other.get_max()) if self and other else False

    @property
    def heap_size(self):
        return len(self.heap)

    @staticmethod
    def parent_idx(curr_idx):
        return (curr_idx - 1) // 2

    @staticmethod
    def left_child_idx(curr_idx):
        return curr_idx * 2 + 1

    @staticmethod
    def right_child_idx(curr_idx):
        return curr_idx * 2 + 2

    def insert(self, val: object):
        # Add a value as the last node of out Complete Binary Tree
        self.heap.append(val)
        # Fix heap in order to satisfy a max-heap property
        self._heapify_up(self.heap_size - 1)

    def get_max(self) -> object:
        return None if not self.heap else self.heap[0]

    def remove_max(self) -> object:
        if self.heap_size == 0:
            raise IndexError(f'remove_max from an empty {self.__class__.__name__}')
        # Store a value to be returned
        removed = self.heap[0]
        # Place the last leaf in the root position
        last = self.heap.pop()
        if self.heap_size > 0:
            self.heap[0] = last
            # Fix a heap in order to stisfy a max-heap property
            self._heapify_down(0, self.heap_size)
        return removed

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, curr_idx, end_idx=0):
        while curr_idx > end_idx:
            parent_idx = self.parent_idx(curr_idx)
            if self.heap[curr_idx] > self.heap[parent_idx]:
                self.swap(curr_idx, parent_idx)
            curr_idx = parent_idx

    def _heapify_down(self, curr_idx, end_idx):
        while True:
            l = self.left_child_idx(curr_idx)
            r = self.right_child_idx(curr_idx)
            largest_idx = curr_idx

            if l < end_idx:
                if self.heap[l] > self.heap[curr_idx]:
                    largest_idx = l
                if r < end_idx and self.heap[r] > self.heap[largest_idx]:
                    largest_idx = r

            if largest_idx != curr_idx:
                self.swap(curr_idx, largest_idx)
                curr_idx = largest_idx
            else:
                break

    def build_heap(self):
        for i in range(self.heap_size // 2 - 1, -1, -1):
            self._heapify_down(i, self.heap_size)


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, values: 'iterable' = None):
        self.head = self.tail = None
        self.length = 0
        values and self.extend(values)  # The same as 'if values: self.extend(values)'

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.val
            curr = curr.next

    def __str__(self):
        return ' -> '.join(map(str, self))

    def __len__(self):
        return self.length

    def insert_node_sorted(self, node, prev_node=None):
        if not self:
            self.head = self.tail = node
        else:
            if not prev_node and node.val >= self.head.val:
                node.next = self.head
                self.head = node
            elif not prev_node and node.val <= self.tail.val:
                self.tail.next = node
                self.tail = node
            else:
                # Traverse to the appropriate position
                curr = prev_node or self.head
                while curr.next and node.val < curr.next.val:
                    curr = curr.next
                node.next = curr.next
                curr.next = node
        self.length += 1

    def remove_node_after(self, prev_node: Node):
        if prev_node.next is self.tail:
            self.tail = prev_node
        prev_node.next = prev_node.next.next
        self.length -= 1


def steal_bricks(own_bricks, other_bricks):
    towers = LinkedList()
    # Build own tower (calculate its current height)
    own_height = sum(own_bricks)
    max_height = 0
    # Build towers of other children
    for bricks in other_bricks:
        height = sum(bricks)
        tower = MaxHeap(bricks)
        towers.insert_node_sorted(Node([height, tower]))
        max_height = max(max_height, height)
    # Check if already we are the winner
    if own_height > max_height:
        return []  # No bricks need to be stolen

    stolen = []
    while own_height <= max_height:
        # Handle the highest tower separately (the case in which we take the highest
        # brick of the currently highest tower)
        max_height, curr_tower = towers.head.val
        new_highest = max_height - curr_tower.get_max()
        if towers.head.next and towers.head.next.val[0] > new_highest:
            new_highest = towers.head.next.val[0]
        best_choice_prev = None  # That will mean we choose the highest tower
        remaining_height = new_highest - (own_height + curr_tower.get_max())

        # Check if it's better to take a brick from another tower
        prev_tower = towers.head
        while prev_tower.next:
            _, curr_tower = prev_tower.next.val
            curr_remaining = max_height - (own_height + curr_tower.get_max())
            if curr_remaining < remaining_height:
                remaining_height = curr_remaining
                best_choice_prev = prev_tower
            prev_tower = prev_tower.next

        # Now we have to update own tower's height and steal the chosen brick from
        # the chosen tower
        # If the previous tower to the chosen one is None (we chose the highest tower)
        if best_choice_prev is None:
            towers.length -= 1
            tower = towers.head
            towers.head = towers.head.next
            max_height = new_highest
        # Else, if the choosen tower isn't the highest one
        else:
            tower = best_choice_prev.next
            towers.remove_node_after(best_choice_prev)

        tower.next = None
        stolen_brick = tower.val[1].remove_max()
        tower.val[0] -= stolen_brick
        # If a tower hasn't been exhausted yet, insert it again
        if tower.val[0] > 0:
            towers.insert_node_sorted(tower, best_choice_prev)
        own_height += stolen_brick
        stolen.append(stolen_brick)

    return stolen