class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Adds node to the top
    def push(self, data):
        new_node = Node(data)
        temp = self.head

        new_node.next = self.head

        if self.head is None:
            new_node.next = new_node

        else:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node

        self.head = new_node

    # Prints the linked list
    def print(self):
        temp = self.head
        if temp is None:
            print("Linked List is empty")
        else:
            while True:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head:
                    print("HEAD")
                    break


cll = LinkedList()

cll.push(4)
cll.push(3)
cll.push(2)
cll.push(1)
cll.print()
