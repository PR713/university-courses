class SegmentTree:
    def __init__(self, arrayLen, storehouseCapacity) -> None:
        numberOfLeaves = 1
        while numberOfLeaves < arrayLen:
            numberOfLeaves <<= 1  # same as: numberOfLeaves *= 2

        self.firstLeaveIdx = numberOfLeaves - 1
        self.segmentTree = [storehouseCapacity for _ in range(2 * numberOfLeaves - 1)]

    def add_coal(self, amount):
        node = 0

        # find storehous
        while node < self.firstLeaveIdx:
            left = 2 * node + 1
            right = 2 * node + 2
            if self.segmentTree[left] >= amount:
                node = left
            else:
                node = right

        storehouseIdx = node - self.firstLeaveIdx

        self.segmentTree[node] -= amount

        while node > 0:
            node = (node - 1) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            self.segmentTree[node] = max(self.segmentTree[left], self.segmentTree[right])

        return storehouseIdx


def coal(A, T):
    # tu prosze wpisac wlasna implementacje
    n = len(A)
    segTree = SegmentTree(n, T)

    for i in range(n - 1):
        segTree.add_coal(A[i])

    return segTree.add_coal(A[n - 1])