print("Doublely Linked List:")
class DoublelyLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
def insert(head):
    if head is None:
        print("Doublely Linked List is Empty")
    else:
        new_node = DoublelyLinkedList(4)
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

def Traversal(head):
    current = head
    while current is not None:
        print(current.data, end=" ↔ ")
        current = current.next
    print("None")

def search(node):
    if node:
        return "Empty Tree"
    else:
        pass

node1 = DoublelyLinkedList(10)        
node2 = DoublelyLinkedList(20)
node3 = DoublelyLinkedList(30)
node1.next = node2
node2.next = node3
node2.prev = node1
node3.prev = node2
Traversal(node1) 
search(30)   
