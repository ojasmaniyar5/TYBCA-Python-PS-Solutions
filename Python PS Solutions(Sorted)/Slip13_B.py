class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(f"Queue: {self.queue}")

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
