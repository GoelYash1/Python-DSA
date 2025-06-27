class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []
    
    def print_stack(self):
        for item in reversed(self.items):
            print(item, end="->")
        print()
    
# example usage
if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)

    print("Stack height:", len(my_stack.items))
    print("Stack contents:")
    my_stack.print_stack()

    print("Top element:", my_stack.peek())
    
    popped_item = my_stack.pop()
    print("Popped item:", popped_item)
    
    print("Stack after popping:")
    my_stack.print_stack()
    
    my_stack.clear()
    print("Stack after clearing:")
    my_stack.print_stack()
    
