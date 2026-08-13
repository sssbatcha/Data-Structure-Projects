class BSTNode:
    def __init__(self, data):       
        self.data = data
        self.left = None
        self.right = None
def insert(root, data):
    if root is None:
        return BSTNode(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.data, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)  

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=' ')     
root = None
values = [50, 30, 20, 40, 70, 60, 80]
for value in values:
    root = insert(root, value)                      


print("Inorder Traversal of the BST:")
inorder_traversal(root) 
print("\nPreorder Traversal of the BST:")
preorder_traversal(root)
print("\nPostorder Traversal of the BST:")
postorder_traversal(root)