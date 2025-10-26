from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def count_on_level(T): #zlicza liczbę
    #node'ów na każdym poziomie
    levels = []

    def visit(R, level):
        if len(levels) == level:
            levels.append(1)
        else:
            levels[level] += 1

        if R.left:
            visit(R.left, level + 1)
        if R.right:
            visit(R.right, level + 1)

    visit(T, 0)
    return levels


def visit(T, max_level):
    def dfs(node, lvl):
        if node is None: return
        if node.left: dfs(node.left, lvl + 1)
        if node.right: dfs(node.right, lvl + 1)

        if node.left is None and node.right is None:
            node.x = True   #True czyli liść
        else:
            if node.left is not None and node.right is not None:
                node.x = node.left.x and node.right.x #True czyli ich
                #dzieci są liśćmi
            elif node.left is not None:
                node.x = node.left.x
            else:
                node.x = node.right.x

        if lvl == max_level: node.x = False

    dfs(T, 0)


def erase(T):
    res = 0
    #zlicza liczbę liści w drzewie T
    # oznaczonych jako .x = True
    def visit(node):
        nonlocal res
        if node.x:
            res += 1
        else:
            if node.right is not None:
                visit(node.right)
            if node.left is not None:
                visit(node.left)

    visit(T)
    return res


def wideentall_1(T):
    levels = count_on_level(T)
    n = len(levels)
    max_level = n - 1
    max_val = levels[-1]
    for i in range(n - 1, -1, -1):
        if levels[i] > max_val:
            max_level = i
            max_val = levels[i]

    visit(T, max_level)
    sol = erase(T)
    return sol


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall_1, all_tests = False )