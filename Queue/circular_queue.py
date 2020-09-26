# Rear + 1 % Size = Front

class Queue:
    def __init__(self, size):
        self.items = [None for i in range(size)]
        self.size = size
        self.rear = self.front = -1

	def enqueue(self, data):
		if (self.rear+1 % self.size) == self.front:
			print("Queue is full")
			return
		elif self.front == -1:
			self.front = 0
			self.rear = 0
			self.list[self.rear] = data
		else:
			self.rear = (self.rear + 1) % self.size
			self.list[self.rear] = data

	def dequeue(self):
		if self.front == -1:
			print("Queue is empty")
			return
		elif self.front == self.rear:
			val = self.list[self.front]
			self.front = -1
			self.rear = -1
			return val
		else:
			val = self.list[self.front]
			self.front = (self.front + 1) % self.size
			return val