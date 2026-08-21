print("Implementation of Queue using Linked List in Python ")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def enqueue(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return head
    else:
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head
def dequeue(head):
    if head is None:
        print("Queue is empty")
        return head
    else:
        head = head.next
        return head
def display(head):
    if head is None:
        print("Queue is empty")
    else:
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
node = None
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to enqueue: "))
        node = enqueue(node, data)
    elif choice == 2:
        node = dequeue(node)
    elif choice == 3:
        display(node)
    elif choice == 4:
        break
    else:
        print("Invalid choice")