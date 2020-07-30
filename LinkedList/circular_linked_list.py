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

    # Adds node to the last
    def append(self, data):
        new_node = Node(data)
        temp = self.head

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return

        while True:
            if temp.next == self.head:
                break
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

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

    # Deletes the element
    def delete(self, delete_value):
        current_node = self.head
        prev_node = None

        while current_node:
            # Deletes the Head
            if current_node.data == delete_value and current_node == self.head:
                # Head is the only element
                if current_node.next == self.head:
                    current_node = None
                    self.head = None
                    return
                # More elements are there
                else:
                    # Traverse and deletes
                    while current_node.next != self.head:
                        current_node = current_node.next
                    current_node.next = self.head.next
                    self.head = self.head.next
                    current_node = None
                    return
                pass
            # Regular Case
            elif current_node.data == delete_value:
                prev_node.next = current_node.next
                current_node = None
                return
            # Node not found
            else:
                if current_node.next == self.head:
                    print("Node not found")
                    return

            # updates the previous node and the current node
            prev_node = current_node
            current_node = current_node.next

    # Counts the number of nodes
    def count(self):
        current = self.head
        counter = 1
        while(current.next != self.head):
            counter += 1
            current = current.next
        print("Count is: ", str(counter))

    # Converts a linked list to a circular linked list
    def convertLinkedListToCircular(self, head):
        current = head

        while current.next is not None:
            current = current.next

        current.next = head
        return head


cll = LinkedList()

cll.push(4)
cll.push(3)
cll.push(2)
cll.push(1)
cll.delete(4)
cll.append(4)
cll.count()
cll.print()
