class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        for i in range(self.size()):
            print(self.items[i], ',', end='')
        print('\n')


# Example usage
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.display()

    print("Queue size:", queue.size())
    print("Front element:", queue.peek())

    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    queue.display()
    print("Queue size after dequeue:", queue.size())
