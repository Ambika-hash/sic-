class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full!")
        elif self.front == -1:  # First element
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty!")
        elif self.front == self.rear:
            print(f"Dequeued: {self.queue[self.front]}")
            self.front = self.rear = -1
        else:
            print(f"Dequeued: {self.queue[self.front]}")
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is Empty!")
        else:
            print("Circular Queue:", end=" ")
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()

q = CircularQueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
q.dequeue()
q.enqueue(50)
q.enqueue(60)
q.display()
q.enqueue(70)  
