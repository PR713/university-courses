
#zaproponuj strukturę danych
#-insert
#-removemin
#-removemax     / O(log(n))
#ale jakby która obsługuje w takim czasie podane
#operacje, bo samo zrobienie kopca i tak nlogn
#TO JEST STRUKTURA DOUBLE HEAP a nie MIN-MAX-HEAP!!!
#https://en.wikipedia.org/wiki/Double-ended_priority_queue
class MinMaxHeap:
    minHeap = []
    maxHeap = []

    def __init__(self, tab: list) -> None:
        n = len(tab)
        self.minHeap: list[list[int]] = [[tab[i], i] for i in range(n)]
        self.maxHeap: list[list[int]] = [[tab[i], i] for i in range(n)]
        self.build_max_heap()
        self.build_min_heap()

    #####################
    #       core        #
    #####################

    def insert(self, val):
        self.add_min_heap(val)
        self.add_max_heap(val)

    # removes min value and returns it
    def remove_min(self) -> int:
        n = len(self.minHeap)
        minVal, minIndex = self.minHeap[0]
        self.swap_min_elements(0, n - 1)
        self.swap_max_elements(minIndex, n - 1)
        self.minHeap.pop()
        self.heapify_min(n - 2, 0)
        parentInMaxHeap = (minIndex - 1) // 2
        if minIndex > 0 and self.maxHeap[minIndex][0] > self.maxHeap[parentInMaxHeap][0]:
            self.repair_max_heap(minIndex)
        else:
            self.heapify_max(n - 2, minIndex)
        self.maxHeap.pop()

        return minVal

    # removes max value and returns it
    def remove_max(self) -> int:
        n = len(self.maxHeap)
        maxVal, maxIndex = self.maxHeap[0]
        self.swap_max_elements(0, n - 1)
        self.swap_min_elements(maxIndex, n - 1)
        self.maxHeap.pop()
        self.heapify_max(n - 2, 0)
        parentInMinHeap = (maxIndex - 1) // 2
        if maxIndex > 0 and self.minHeap[maxIndex][0] < self.minHeap[parentInMinHeap][0]:
            self.repair_min_heap(maxIndex)
        else:
            self.heapify_min(n - 2, maxIndex)
        self.minHeap.pop()

        return maxVal

    #################
    #   max heap    #
    #################

    def build_max_heap(self):
        n = len(self.maxHeap)
        for i in range(n - 1, -1, -1):
            self.heapify_max(n - 1, i)

    def heapify_max(self, lastIndex, toFix):
        maxi = None
        while True:
            maxi = toFix
            left = 2 * toFix + 1
            right = 2 * toFix + 2

            if left <= lastIndex and self.maxHeap[left][0] > self.maxHeap[maxi][0]:
                maxi = left

            if right <= lastIndex and self.maxHeap[right][0] > self.maxHeap[maxi][0]:
                maxi = right

            if toFix == maxi:
                break
            else:
                self.swap_max_elements(toFix, maxi)
                toFix = maxi

    def swap_max_elements(self, index1, index2):
        self.maxHeap[index1], self.maxHeap[index2] = self.maxHeap[index2], self.maxHeap[index1]
        indexInMinHeap1 = self.maxHeap[index1][1]
        indexInMinHeap2 = self.maxHeap[index2][1]
        self.minHeap[indexInMinHeap1][1] = index1
        self.minHeap[indexInMinHeap2][1] = index2

    def add_max_heap(self, val):
        n = len(self.maxHeap)
        self.maxHeap.append([val, n])
        self.repair_max_heap(len(self.maxHeap) - 1)

    def repair_max_heap(self, toRepair):
        parent = None
        while toRepair > 0:
            parent = (toRepair - 1) // 2
            if self.maxHeap[toRepair][0] > self.maxHeap[parent][0]:
                self.swap_max_elements(toRepair, parent)
                toRepair = parent
            else:
                break
            # end if
        # end while

    #################
    #   min heap    #
    #################

    def build_min_heap(self):
        n = len(self.minHeap)
        for i in range(n - 1, -1, -1):
            self.heapify_min(n - 1, i)

    def heapify_min(self, lastIndex, toFix):
        mini = None
        while True:
            mini = toFix
            left = 2 * toFix + 1
            right = 2 * toFix + 2

            if left <= lastIndex and self.minHeap[left][0] < self.minHeap[mini][0]:
                mini = left

            if right <= lastIndex and self.minHeap[right][0] < self.minHeap[mini][0]:
                mini = right

            if toFix == mini:
                break
            else:
                self.swap_min_elements(toFix, mini)
                toFix = mini

    def swap_min_elements(self, index1, index2):
        self.minHeap[index1], self.minHeap[index2] = self.minHeap[index2], self.minHeap[index1]
        indexInMaxHeap1 = self.minHeap[index1][1]
        indexInMaxHeap2 = self.minHeap[index2][1]
        self.maxHeap[indexInMaxHeap1][1] = index1
        self.maxHeap[indexInMaxHeap2][1] = index2

    def add_min_heap(self, val):
        n = len(self.minHeap)
        self.minHeap.append([val, n])
        self.repair_min_heap(len(self.minHeap) - 1)

    def repair_min_heap(self, toRepair):
        parent = None
        while toRepair > 0:
            parent = (toRepair - 1) // 2
            if self.minHeap[toRepair][0] < self.minHeap[parent][0]:
                self.swap_min_elements(toRepair, parent)
                toRepair = parent
            else:
                break
            # end if
        # end while

    def print_heap(self):
        n = len(self.maxHeap)
        print("maxHeap: ", end="")
        for i in range(n - 1):
            print(self.maxHeap[i][0], end=", ")
        print(self.maxHeap[n - 1][0])

        print("minHeap: ", end="")
        for i in range(n - 1):
            print(self.minHeap[i][0], end=", ")
        print(self.minHeap[n - 1][0])

        # print(f"maxHeap: {self.maxHeap}")
        # print(f"minheap: {self.minHeap}")


if __name__ == "__main__":
    testTab = [2, 3, 1, 5, 6]
    # testTab = [2,3,1]
    testHeap = MinMaxHeap(testTab)
    testHeap.print_heap()
    testHeap.insert(4)
    testHeap.print_heap()
    print("min:", testHeap.remove_min())
    testHeap.print_heap()
    print("max:", testHeap.remove_max())
    testHeap.print_heap()
