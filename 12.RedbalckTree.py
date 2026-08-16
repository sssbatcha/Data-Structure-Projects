print("RedBlackTree:")
class redblacktreeNode:
    
    def __init__(self, data):
        self.data = data
        self.color = 1  # 1 for Red, 0 for Black
        self.left = None
        self.right = None
        self.parent = None




def left_rotate(new_node):
    right_child = new_node.right
    new_node.right = right_child.left

    if right_child.left is not None:
        right_child.left.parent = new_node

    right_child.parent = new_node.parent

    if new_node.parent is None:
        global root
        root = right_child
    elif new_node == new_node.parent.left:
        new_node.parent.left = right_child
    else:
        new_node.parent.right = right_child

    right_child.left = new_node
    new_node.parent = right_child

def right_rotate(new_node):
    left_child = new_node.left
    new_node.left = left_child.right

    if left_child.right is not None:
        left_child.right.parent = new_node

    left_child.parent = new_node.parent

    if new_node.parent is None:
        global root
        root = left_child
    elif new_node == new_node.parent.right:
        new_node.parent.right = left_child
    else:
        new_node.parent.left = left_child

    left_child.right = new_node
    new_node.parent = left_child









def fix_violation(new_node):
    while new_node != root and new_node.parent.color == 1:
        if new_node.parent == new_node.parent.parent.left:
            uncle = new_node.parent.parent.right
            if uncle and uncle.color == 1:  # Case 1: Uncle is red
                new_node.parent.color = 0
                uncle.color = 0
                new_node.parent.parent.color = 1
                new_node = new_node.parent.parent
            else:
                if new_node == new_node.parent.right:  # Case 2: New node is right child
                    new_node = new_node.parent
                    left_rotate(new_node)
                # Case 3: New node is left child
                new_node.parent.color = 0
                new_node.parent.parent.color = 1
                right_rotate(new_node.parent.parent)
        else:
            uncle = new_node.parent.parent.left
            if uncle and uncle.color == 1:  # Case 1: Uncle is red
                new_node.parent.color = 0
                uncle.color = 0
                new_node.parent.parent.color = 1
                new_node = new_node.parent.parent
            else:
                if new_node == new_node.parent.left:  # Case 2: New node is left child
                    new_node = new_node.parent
                    right_rotate(new_node)
                # Case 3: New node is right child
                new_node.parent.color = 0
                new_node.parent.parent.color = 1
                left_rotate(new_node.parent.parent)
    root.color = 0

def insert(root):
    new_node = redblacktreeNode(root)
    new_node.color = 1  # New node must be red
    new_node.left = None
    new_node.right = None
    new_node.parent = None

    if root is None:
        new_node.color = 0  # If tree is empty, make the new node black
        return new_node

    current = root
    while True:
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right

    new_node.parent = current
    fix_violation(new_node)
    return root

root = None
root = insert(10)
root = insert(50)
root = insert(150)
root = insert(110)


