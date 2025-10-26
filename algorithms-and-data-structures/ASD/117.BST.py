class BSTNode:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.parent = self.left = self.right = None

def search(node,key):
    while node != None:
        if node.key == key: return node
        elif node.key < key: node = node.right
        else: node = node.left
    return None