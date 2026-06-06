class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def checkEmpty(self):
        return self.head is None

    def insert_at_head(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def traverse(self):
        if self.checkEmpty():
            print("DLL is Empty")
            return

        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()

    def deleteatlast(self):
        if self.checkEmpty():
            print("DLL is Empty")
            return

        # Only one node
        if self.head.next is None:
            self.head = None
            return

        current = self.head

        # Move to last node
        while current.next is not None:
            current = current.next

        # Remove last node
        current.prev.next = None

    def insert_at_index(self, value, index):
        new_node = Node(value)
        if index == 0:
            self.insert_at_head(value)
            return
        
        current = self.head
        count = 0

        while current and count < index - 1:
            current = current.next
            count += 1

        if current is None:
            print("Index out of Bounds")

        new_node.prev = current
        new_node.next = current.next

        if current.next:
            current.next.prev = new_node

        current.next = new_node


# Driver Code
dll = DoublyLinkedList()

dll.traverse()      # Empty list

dll.insert_at_head(3)
dll.insert_at_head(6)
dll.insert_at_head(1)
dll.insert_at_head(9)

print("Before deletion:")
dll.traverse()

dll.deleteatlast()

print("After deleting last node:")
dll.traverse()

dll.insert_at_index(11, 1)
dll.traverse()