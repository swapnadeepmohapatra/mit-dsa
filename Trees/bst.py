class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class BinarySearchTree:
    def __init__(self, root = None):
        self.root = Node(root)

    def insert_helper(self, this_node, data):
        if data > this_node.data:
            # Insert the node at Right
            if this_node.right is None:
                this_node.right = Node(data)
            else:
                self.insert_helper(this_node.right, data)
        if data < this_node.data:
            # Insert the node at Left
            if this_node.left is None:
                this_node.left = Node(data)
            else:
                self.insert_helper(this_node.left, data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_helper(self.root, data)


def main():
    bst = BinarySearchTree(10)
    bst.insert(10)
    bst.insert(20)

if __name__ == "__main__":
    main()