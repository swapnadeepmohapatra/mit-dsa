# Node is one element of a Linked List
class Node:
    def __init__(self, data):
        # This stores the data
        self.data = data

        # This stores the next pointer. Initially it is None (null)
        self.next = None


# Linked list is a class that contains many Nodes
class LinkedList:

    def __init__(self):
        # Initializes the HEAD
        self.head = None

    # Add node to the start

    def push(self, new_value):
        # Creating a new node by passing on the new data
        new_node = Node(new_value)

        # The next pointer of the new node points to the next pointer of the head
        new_node.next = self.head

        # Declares the new node as head
        self.head = new_node

    # Add node at a particular place

    def insert_at(self, prev_node, new_value):
        temp = self.head

        # Moves to the previous node
        while temp:
            if temp.data == prev_node:
                # Creating a new node by passing on the new data
                new_node = Node(new_value)

                # The next pointer of the new node points to the next pointer of the previous node
                new_node.next = temp.next

                # The next pointer of the previous node points to new node
                temp.next = new_node
                return
            temp = temp.next
        print("No Node found")

    # Adds node to the end

    def append(self, new_value):
        new_value = Node(new_value)

        # Checks if list is empty
        if self.head == None:
            # Initializes the HEAD as the new value
            self.head = new_value
            return

        # Moves to the last node
        last = self.head
        while(last.next):
            last = last.next

        last.next = new_value

    # Delete a node

    def delete(self, value):
        temp = self.head

        # Checks if the node to be deleted is the head itself
        if temp != None:
            if temp.data == value:
                self.head = temp.next
                temp = None
                return

        # Checks if the Linked List is empty
        if temp == None:
            print("Linked List is empty")
            return

        # Traverses through the Linked List
        while temp:

            # Stops at the deleted node
            if temp.data == value:
                break

            # Gets the previous Node
            prev = temp

            # Updates the temp with the next node
            temp = temp.next

        # The next pointer of the previous node points to the next node of the node to be deleted
        prev.next = temp.next

        # Frees up the space
        temp = None

    # Prints the list

    def print_list(self):
        temp = self.head
        # Traverses through the list
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(None)


def main():
    lList = LinkedList()
    lList.push(3)
    lList.push(5)
    lList.push(6)
    lList.push(2)
    lList.insert_at(5, 1)
    lList.delete(5)
    lList.print_list()


if __name__ == "__main__":
    main()
