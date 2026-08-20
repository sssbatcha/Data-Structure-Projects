<<<<<<< HEAD
print("Circular Linked List Implementation in Python")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    if head is None:
        return
    current = head
    while True: 
        print(current.data, end=" -> ")
        current = current.next
        if current == head:
            break

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        new_node.next = new_node
        return new_node
    else:
        current = head
        while current.next != head:
            current = current.next
        current.next = new_node
        new_node.next = head
        return head

def insert_at_beginning(head, data):
    new_node = Node(data)
    if head is None:
        new_node.next = new_node
        return new_node
    else:
        current = head
        while current.next != head:
            current = current.next
        current.next = new_node
        new_node.next = head
        return new_node 

def delete_node(head, key):
    if head is None:
        return None
    current = head
    prev = None
    while True:
        if current.data == key:
            if prev is not None:
                prev.next = current.next
            else:
                # Deleting the head node
                if current.next == head:  # Only one node in the list
                    return None
                else:
                    # Find the last node to update its next pointer
                    last_node = head
                    while last_node.next != head:
                        last_node = last_node.next
                    last_node.next = current.next
                    head = current.next
            return head
        prev = current
        current = current.next
        if current == head:
            break
    return head

root = None
root = insert_at_end(root, 1)
root = insert_at_end(root, 2)
print_list(root)
    


        
=======
print("Circular Linked List Implementation in Python")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    if head is None:
        return
    current = head
    while True: 
        print(current.data, end=" -> ")
        current = current.next
        if current == head:
            break

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        new_node.next = new_node
        return new_node
    else:
        current = head
        while current.next != head:
            current = current.next
        current.next = new_node
        new_node.next = head
        return head

def insert_at_beginning(head, data):
    new_node = Node(data)
    if head is None:
        new_node.next = new_node
        return new_node
    else:
        current = head
        while current.next != head:
            current = current.next
        current.next = new_node
        new_node.next = head
        return new_node 

def delete_node(head, key):
    if head is None:
        return None
    current = head
    prev = None
    while True:
        if current.data == key:
            if prev is not None:
                prev.next = current.next
            else:
                # Deleting the head node
                if current.next == head:  # Only one node in the list
                    return None
                else:
                    # Find the last node to update its next pointer
                    last_node = head
                    while last_node.next != head:
                        last_node = last_node.next
                    last_node.next = current.next
                    head = current.next
            return head
        prev = current
        current = current.next
        if current == head:
            break
    return head

root = None
root = insert_at_end(root, 1)
root = insert_at_end(root, 2)
print_list(root)
    


        
>>>>>>> 34e5631df912f6555ad430ba4e9ab1e261ac8028
