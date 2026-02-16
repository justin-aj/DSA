class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def append(self, data):
        """Add a new node to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        """Display the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete a node with the given data."""
        if self.head is None:
            return "List is Empty"

        current = self.head
        if current.data == data:
            self.head = current.next

        while current.next is not None:
            # print(current.data, data, current.next.data)
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
            if current is None:
                return
            else:
                print("Does not exist")
                return

    def search(self, data):
        current = self.head

        if not current:
            print("The list is empty.")
            return

        while current.next:
            if current.data == data:
                print(f"The node with data {data} was found.")
            current = current.next

# Create a new linked list
ll = LinkedList()

# Append nodes
ll.append(10)
ll.append(20)
ll.append(30)

# Display the list
ll.display()  # Output: 10 -> 20 -> 30 -> None

# Insert at the beginning
ll.insert_at_beginning(5)
ll.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

# Delete a node
print("Delete")
ll.delete(90)
ll.display()  # Output: 5 -> 10 -> 30 -> None

ll.search(20)