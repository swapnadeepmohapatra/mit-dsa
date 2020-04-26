class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)

        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def insert_at(self, prev_node, new_value):
        new_node = Node(new_value)

        temp = self.head

        while temp:
            if temp.data == prev_node:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print("No Node was found")

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def deleteList(self):
        temp = self.head

        while temp:
            next_node = temp.next
            self.head = next_node
            del temp.data
            temp = next_node

    def delete(self, value):
        temp = self.head

        while temp:
            if temp.data == value:
                break

            prev_node = temp
            temp = temp.next

        prev_node.next = temp.next
        temp = None

    def print_list(self):
        last = self.head

        if last == None:
            print("Linked List is empty")

        while last:
            print(last.data, end=" -> ")
            last = last.next
        print(None)


def main():
    ll = LinkedList()
    ll.append(10)
    ll.push(3)
    ll.append(50)
    ll.push(2)
    ll.push(1)
    ll.append(1)
    ll.insert_at(10, 20)
    ll.print_list()
    ll.delete(10)
    ll.print_list()


if __name__ == "__main__":
    main()
