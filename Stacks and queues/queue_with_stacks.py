from stack import Stack

class Queue(Stack):
    def __init__(self):
        super().__init__()
        self.stack_in = Stack()
        self.stack_out = Stack()
    
    def enqueue(self, value):
        self.stack_in.push(value)

    def dequeue(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()

    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()

    def size(self):
        return self.stack_in.size() + self.stack_out.size()
    
    def print_queue(self):
        self.stack_out.print_stack()
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
