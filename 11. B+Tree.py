print("B+ Tree")
class Node:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for number of keys)
        self.leaf = leaf  # True if leaf node
        self.keys = []  # List of keys in the node
        self.children = []  # List of child pointers    
def insert(node, key):
    if len(node.keys) == (2 * node.t) - 1:  # If the node is full
        new_node = Node(node.t, False)  # Create a new node
        new_node.children.append(node)  # Make the old node a child of the new node
        split_child(new_node, 0)  # Split the old node
        insert_non_full(new_node, key)  # Insert the key in the new node
        return new_node  # Return the new root
    else:
        insert_non_full(node, key)  # Insert the key in the current node
        return node  # Return the current root

def insert_non_full(node, key):
    i = len(node.keys) - 1  # Start from the rightmost key
    if node.leaf:  # If it's a leaf node
        node.keys.append(0)  # Create space for the new key
        while i >= 0 and key < node.keys[i]:  # Find the location to insert the new key
            node.keys[i + 1] = node.keys[i]  # Shift keys to the right
            i -= 1
        node.keys[i + 1] = key  # Insert the new key
    else:  # If it's an internal node
        while i >= 0 and key < node.keys[i]:  # Find the child to insert the new key
            i -= 1
        i += 1
        if len(node.children[i].keys) == (2 * node.t) - 1:  # If the child is full
            split_child(node, i)  # Split the child
            if key > node.keys[i]:  # Determine which of the two children to insert into
                i += 1
        insert_non_full(node.children[i], key)  
def split_child(parent, index):
    t = parent.t
    full_child = parent.children[index]  # The child to be split
    new_child = Node(t, full_child.leaf)  # Create a new node
    parent.children.insert(index + 1, new_child)  # Insert the new child into the parent
    parent.keys.insert(index, full_child.keys[t - 1])  # Move the median key up to the parent
    new_child.keys = full_child.keys[t:(2 * t - 1)]  # Give the new child the last t-1 keys of the full child
    full_child.keys = full_child.keys[0:(t - 1)]  # Retain the first t-1 keys in the full child
    if not full_child.leaf:  # If the full child is not a leaf, move its children to the new child
        new_child.children = full_child.children[t:(2 * t)]
        full_child.children = full_child.children[0:t]

root = Node(3, True)  # Create a B+ tree with minimum degree 3
root = insert(root, 10) 
root = insert(root, 20)
root = insert(root, 5)
root = insert(root, 6)

print("Root keys:", root.keys)  # Print the keys in the root node
