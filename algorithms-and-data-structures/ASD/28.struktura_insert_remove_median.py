
#struktura danych
#-remove median
#- insert O(nlogn)

class MedianHeap:
    ###################     Atributes       ####################
    minHeap = []
    maxHeap = []
    ###################     Functions       ####################

    def __init__(self, tab: list) -> None:
        n = len(tab)
        minLen = n // 2
        maxLen = n - minLen
        self.modified_heap_sort(tab, minLen)
        self.minHeap: list = [tab[i] for i in range(maxLen, maxLen + minLen)]
        self.maxHeap: list = [tab[i] for i in range(maxLen)]

    def min_heap_size(self):
        return len(self.minHeap)

    def max_heap_size(self):
        return len(self.maxHeap)

    def insert(self, val):
        if val <= self.maxHeap[0]:
            # dodajemy element do maxHeap
            if self.max_heap_size() > self.min_heap_size():
                self.add_min_heap(self.maxHeap[0])
                self.maxHeap[0] = val
                self.heapify_max(0)
            else:
                self.add_max_heap(val)
        else:
            # dodajemy do minHeap
            if self.min_heap_size() == self.max_heap_size():
                self.add_max_heap(self.minHeap[0])
                self.minHeap[0] = val
                self.heapify_min(0)
            else:
                self.add_min_heap(val)

    def get_median(self):
        return (self.maxHeap[0] + self.minHeap[0]) / 2 if self.min_heap_size() == self.max_heap_size() else \
        self.maxHeap[0]

    def print_heap(self):
        print(f"minHeap: {self.minHeap}")
        print(f"maxHeap: {self.maxHeap}")

    #######################
    #   initialization    #
    #######################
    def modified_heap_sort(self, tab: list, minHeapLen) -> None:
        self.build_heap(tab)
        n = len(tab)
        for i in range(n - 1, n - minHeapLen - 1, -1):
            tab[0], tab[i] = tab[i], tab[0]
            self.heapify(tab, i - 1, 0)

    def build_heap(self, tab: list):
        n = len(tab)
        for i in range(n - 1, -1, -1):
            self.heapify(tab, n - 1, i)

    def heapify(self, tab, lastIndex, toFix) -> None:
        maxi = toFix
        while True:
            maxi = toFix
            left = 2 * toFix + 1
            right = 2 * toFix + 2

            if left <= lastIndex and tab[left] > tab[maxi]:
                maxi = left

            if right <= lastIndex and tab[right] > tab[maxi]:
                maxi = right

            if toFix != maxi:
                tab[maxi], tab[toFix] = tab[toFix], tab[maxi]
                toFix = maxi
            else:
                break

    #################
    #   max heap    #
    #################
    def heapify_max(self, toFix):
        maxi = toFix
        while True:
            left = 2 * toFix + 1
            right = 2 * toFix + 2

            if left <= self.max_heap_size() - 1 and self.maxHeap[left] > self.maxHeap[maxi]:
                maxi = left

            if right <= self.max_heap_size() - 1 and self.maxHeap[right] > self.maxHeap[maxi]:
                maxi = right

            if maxi == toFix:
                break

            self.maxHeap[toFix], self.maxHeap[maxi] = self.maxHeap[maxi], self.maxHeap[toFix]
            toFix = maxi
        # end while

    def repair_max_heap(self, toRepair):
        while toRepair > 0:
            eleParent = (toRepair - 1) // 2
            if self.maxHeap[toRepair] > self.maxHeap[eleParent]:
                self.maxHeap[eleParent], self.maxHeap[toRepair] = self.maxHeap[toRepair], self.maxHeap[eleParent]
                toRepair = eleParent
            else:
                break
            # end if
        # end while

    def add_max_heap(self, val):
        self.maxHeap.append(val)
        self.repair_max_heap(self.max_heap_size() - 1)

    #################
    #   min heap    #
    #################
    def heapify_min(self, toFix):
        mini = toFix
        while True:
            left = 2 * toFix + 1
            right = 2 * toFix + 2

            if left <= self.min_heap_size() - 1 and self.minHeap[left] < self.minHeap[mini]:
                mini = left

            if right <= self.min_heap_size() - 1 and self.minHeap[right] < self.minHeap[mini]:
                mini = right

            if mini == toFix:
                break

            self.minHeap[toFix], self.minHeap[mini] = self.minHeap[mini], self.minHeap[toFix]
            toFix = mini
        # end while

    def repair_min_heap(self, toRepair):
        while toRepair > 0:
            eleParent = (toRepair - 1) // 2
            if self.minHeap[toRepair] < self.minHeap[eleParent]:
                self.minHeap[eleParent], self.minHeap[toRepair] = self.minHeap[toRepair], self.minHeap[eleParent]
                toRepair = eleParent
            else:
                break
            # end if
        # end while

    def add_min_heap(self, val):
        self.minHeap.append(val)
        self.repair_min_heap(self.min_heap_size() - 1)


if __name__ == "__main__":
    testTab = [2, 5, 1, 6, 7, 8]
    # testTab = [5,1,7,2,3,7,1,6,4,7,8,3,7]
    print(testTab)
    print(sorted(testTab))
    myHeap = MedianHeap(testTab)
    myHeap.print_heap()
    print(myHeap.get_median())
    myHeap.insert(13)
    myHeap.print_heap()
    print(myHeap.get_median())
    myHeap.insert(15)
    myHeap.print_heap()
    print(myHeap.get_median())
    myHeap.insert(0)
    myHeap.print_heap()
    print(myHeap.get_median())