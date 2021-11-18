
def Height(root):
    if root == None:
        return 0
    elif root.left == None and root.right == None:
        return 0
    else:
        HeightL = Height(root.left)
        HeightR = Height(root.right)

    return max(HeightL,HeightR) + 1

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node6 = Node(6)
Node7 = Node(7)
Node8 = Node(8)
Node9 = Node(9)

root = None
Node1.left = Node2
Node1.right = Node3
Node2.left = Node4
Node2.right = Node5
Node3.left = Node6
Node3.right = Node7
Node4.left = Node8
Node4.right = Node9
root = Node1
print(Height(root))

