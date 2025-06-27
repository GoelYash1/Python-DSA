class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def is_empty(self):
        return self.length == 0
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.length -= 1
        return value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.value

    def size(self):
        return self.length
    
    def print_queue(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print("Queue:", " -> ".join(map(str, elements)))

# Example usage
if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)

    my_queue.print_queue()
    print("Peek the Front element:", my_queue.peek())
    print("Queue size:", my_queue.size())
    my_queue.print_queue()

    print("Dequeued element:", my_queue.dequeue())
    print("Queue size after dequeue:", my_queue.size())
    my_queue.print_queue()

    my_queue.enqueue(4)
    my_queue.enqueue(5)
    print("Queue after enqueuing 4 and 5:")
    my_queue.print_queue()

    print("Front element after enqueuing:", my_queue.peek())
    print("Final queue size:", my_queue.size())
    my_queue.print_queue()
