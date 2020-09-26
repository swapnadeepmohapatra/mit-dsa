# Approach 1
class _Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        self.items.pop(0)


q = _Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.items)
q.dequeue()
print(q.items)


# Approach 2

from collections import deque

qu = deque()
qu.append(1)
qu.append(2)
qu.append(3)
print(qu)
qu.popleft()
print(qu)


# Approach 3

from queue import Queue

que = Queue()
que.put(1)
que.put(2)
que.put(3)
print(que)
que.get()
print(que)
