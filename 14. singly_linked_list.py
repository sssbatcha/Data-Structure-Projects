print("Singly Linked List:")
class SinglyLinkedListNodes:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert(head):
    new_node = SinglyLinkedListNodes(4)
    if head is None:
        head = new_node
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
    return head

def Traversal(head):
    current = head
    while current is not None:
        print(current.data, end=" → ")
        current = current.next
    print("None")

node1 = SinglyLinkedListNodes(10)
node2 = SinglyLinkedListNodes(20)
node3 = SinglyLinkedListNodes(30)
node1.next = node2
node2.next = node3
Traversal(node1)