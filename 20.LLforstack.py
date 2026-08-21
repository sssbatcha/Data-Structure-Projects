print("Implementation of Stack using Linked List in Python ")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def push(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

def pop(head):
    if head is None:
        print("Stack is empty")
        return head
    else:
        head = head.next
        return head 

def display(head):
    if head is None:
        print("Stack is empty")
    else:
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
def peek(head):
    if head is None:
        print("Stack is empty")
    else:
        print("Top element is:", head.data)


def is_empty(head):
    return head is None     

node = None
while True: 
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Peek")
    print("5. Is Empty")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to push: "))
        node = push(node, data)
    elif choice == 2:
        node = pop(node)
    elif choice == 3:
        display(node)
    elif choice == 4:
        peek(node)
    elif choice == 5:
        if is_empty(node):
            print("Stack is empty")
        else:
            print("Stack is not empty")
    elif choice == 6:
        break
    else:
        print("Invalid choice")

        