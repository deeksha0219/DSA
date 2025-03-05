class Node:
    def __init__(self, data):
        self.data = data  # Data to store in the node
        self.next = None  # Pointer to the next node (initially None)

class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # 1. Append a node to the end of the list
    def append_node(self, data):
        new_node = Node(data)  # Create a new node with given data
        if not self.head:
            # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            # Traverse to the end of the list
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            # Append the new node at the end
            last_node.next = new_node

    # 2. Search for a node with a particular value
    def search_node(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True  # Node with the data found
            current_node = current_node.next
        return False  # Node with the data not found

    # 3. Display the list
    def display_list(self):
        current_node = self.head
        if not current_node:
            print("The list is empty.")
        else:
            while current_node:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print("None")  # End of list

# Testing the implementation
if __name__ == "__main__":
    linked_list = LinkedList()

    # Appending nodes
    linked_list.append_node(10)
    linked_list.append_node(20)
    linked_list.append_node(30)

    # Display the list
    print("Linked List:")
    linked_list.display_list()

    # Searching for nodes
    print("\nSearching for 20 in the list:")
    if linked_list.search_node(20):
        print("Node with value 20 found.")
    else:
        print("Node with value 20 not found.")

    print("\nSearching for 40 in the list:")
    if linked_list.search_node(40):
        print("Node with value 40 found.")
    else:
        print("Node with value 40 not found.")

