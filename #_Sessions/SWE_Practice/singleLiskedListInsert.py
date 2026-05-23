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

    def insert_at_index(self, value, index):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < index:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current

    def delete(self, value):

        temp = self.head
        if temp.next is not None:
            if temp.value == value:
                self.head = temp.next
                return
            
            else:
                found = False
                prev = None

                while temp is not None:
                    if temp.value == value:
                        found = True
                        break

                    prev = temp
                    temp = temp.next

                if found:
                    prev.next = temp.next
                    return
                
                else:
                    print("Node not Found")

sll = SinglyLinkedList()
# sll.traverse()
sll.append(2)
sll.append(20)
sll.append(10)
# sll.append(1)
sll.traverse()
sll.insert_at_index(50, 1)
sll.traverse()
sll.delete(20)
sll.traverse()
