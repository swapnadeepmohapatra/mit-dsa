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

        # initialize the current node
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

        # initialize the new node
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

        # initialize the current node
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

    # Delete the whole Linked List

    def deleteList(self):

        # initialize the current node
        temp = self.head

        # Traverses through the list
        while temp:
            # Moves to the next Node
            next_node = temp.next

            # Asigns the null to the head
            self.head = next_node

            # Deletes the value in the Node
            del temp.data

            # Sets temp to the next node
            temp = next_node

    # Prints the list

    def print_list(self):

        # initialize the current node
        temp = self.head

        # Checks if the List is Empty
        if temp == None:
            print("Empty List")

        # Traverses through the list
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(None)

    # Gets the count of the node

    def get_node_count(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.get_node_count(node.next)

    def get_count(self):
        return self.get_node_count(self.head)


def main():
    lList = LinkedList()
    lList.push(3)
    lList.push(5)
    lList.push(6)
    lList.push(2)
    lList.insert_at(5, 1)
    # lList.delete(5)
    # lList.deleteList()
    lList.print_list()
    print(lList.get_count())


if __name__ == "__main__":
    main()
