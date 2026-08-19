print("Greedy Algorithms:")
def GreedyTraversal(head):
    current = head
    while current is not None:
        print(current.data, end=" ↔ ")
        current = current.next
    print("None")

def insert(head):
    if head is None:
        print("Greedy Algorithms is Empty")
    else:
        new_node = GreedyAlgorithms(4)
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current



def search(node):
    if node:
        return "Empty Tree"
    else:
        pass

root = GreedyAlgorithms(10)
node2 = GreedyAlgorithms(20)
root.next = node2
GreedyTraversal(root)
    