# creating single linked list 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    
class SinglyLinkedList():
    def __init__(self):
        self.head = None

    # SLL Empty

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node

        else:
            current = self.head
            while current.next is not None: 
                current = current.next

            current.next = new_node

    def traverse(self):
        if not self.head:
            print("SLL is Empty")
        else:
            current = self.head
            while current is not None:
                print(current.value, end=" ")
                current = current.next
            print()


# node1 = Node(5)
# node2 = Node(2)
# node3 = Node(8)

# node1.next = node2
# node2.next = node3

# print(node1)
# print(node1.value)
# print(node1.next)
# print(node1.next.next.value)

sll = SinglyLinkedList()
sll.traverse()
sll.append(2)
sll.append(20)
sll.append(10)
sll.append(1)
sll.traverse()

