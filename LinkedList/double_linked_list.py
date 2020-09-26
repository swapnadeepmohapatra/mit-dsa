import gc


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head

        if self.head is not None:
            # new_node.prev = self.head.prev
            self.head.prev = new_node

        self.head = new_node

    def insert_after(self, prev_node, value):
        if prev_node is None:
            print("prev_node cannot be None")
            return

        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, value):
        new_node = Node(value)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node
        new_node.prev = last_node

    def delete(self, value):
        if self.head is None or value is None:
            print("Error")
            return

        temp = self.head

        if self.head.data == value:
            self.head = temp.next
            del temp
            return

        while temp:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp.prev is not None:
            temp.prev.next = temp.next

            del temp

    def print(self):
        node = self.head

        while node is not None:
            print(node.data, end=" -> ")
            node = node.next

        print("None")


def main():
    dlList = LinkedList()
    dlList.push(5)
    dlList.push(6)
    dlList.push(7)
    dlList.append(9)
    dlList.print()
    dlList.delete(9)
    dlList.print()


if __name__ == "__main__":
    main()
