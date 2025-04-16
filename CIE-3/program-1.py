def __init__(self, data):
        self.data = data 
        self.next = None  

class CircularLinkedList:
    def __init__(self):
        self.head = None 

    def insert_at_beginning(self, data):
        new_node = new_node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
                current.next = new_node
                new_node.next = self.head
                self.head = new_node

    def delete(self, key):
        if self.head is None:
            print("List is empty!")
            return
        
        current = self.head

        if current.data == key and current.next == self.head:
            self.head = None
            return

        prev = None

        while current.next != self.head:
            if current.data == key:
                break
            prev = current
            current = current.next

        if current.data != key:
            print(f"Node with value {key} not found.")
            return

        if current == self.head:
            prev = self.head
            while prev.next != self.head:
                prev = prev.next
            self.head = current.next
            prev.next = self.head
        else:
            prev.next = current.next

    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(f"(head)")


cll = CircularLinkedList()
cll.insert_at_beginning(10)
cll.insert_at_beginning(20)
cll.insert_at_beginning(30)

cll.display() 
cll.delete_node(10)
cll.display()  
