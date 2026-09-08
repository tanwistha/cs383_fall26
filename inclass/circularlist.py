class Node:
    def __init__(self, data):
        self.data  = data
        self.next = None

class CircularList:
    def __init__(self):
        # Initialize an empty circular linked list with head pointer pointing to None
        self.head = None


    def insert(self, data):
        # Append a new node with data to the end of the circular linked list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
     
    def traverse(self):
        # Traverse and display the elements of the circular linked list
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head:
                break

l = CircularList()
print("insert node..")
l.insert(1)
l.insert(2)
l.insert(3)
l.traverse()
print("inserting again..")
l.insert(4)
l.traverse()