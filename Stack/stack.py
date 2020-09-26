# Self Implementation
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if len(self.items) == 0:
            print("Stack is Empty")
        else:
            self.items.pop()


s = Stack()
s.push(5)
s.push(6)
s.push(7)
print(s.items)
s.pop()
print(s.items)
s.pop()
print(s.items)
