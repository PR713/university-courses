class Node:
    def __init__( self ):
        self.left = None    # lewe poddrzewo
        self.right = None   # prawe poddrzewo
        self.x = None       # pole do wykorzystania przez studentow # wysokość

def add_height(curr,height):
    if curr!=None:
        curr.x=height
        return max(add_height(curr.left,height+1),add_height(curr.right,height+1))
    return height

def add_width(curr,width):
    if curr!=None:
        width[curr.x]+=1
        add_width(curr.left,width)
        add_width(curr.right,width)

def remove_below(curr,height,cuts):
    if curr.x==height:
        if curr.right:
            cuts[0]+=1
            curr.right=None
        if curr.left:
            cuts[0]+=1
            curr.left=None
    if curr.right:
        remove_below(curr.right,height,cuts)

    if curr.left:
        remove_below(curr.left,height,cuts)

def remove_rest(curr,height,cuts):
    if curr!=None:
        if curr.x<height:
            cuts[0]+=1
            return 0
        remove_rest(curr.right,height,cuts)
        remove_rest(curr.left,height,cuts)

def change_tag(curr):
    if curr==None:
        return 0
    if curr.left==None and curr.right==None:
        return curr.x
    curr.x=max(change_tag(curr.left),change_tag(curr.right))
    return curr.x

def wideentall( T ):
    height=add_height(T,0)
    width=[0 for _ in range(height)]
    add_width(T,width)
    maxi=max(width)
    n=height
    cuts=[0]
    for i in range(n-1,-1,-1):
        if width[i]==maxi:
            height=i
            break

    remove_below(T,height,cuts)
    change_tag(T)
    remove_rest(T,height,cuts)
    return cuts[0]
