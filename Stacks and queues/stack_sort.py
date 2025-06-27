from stack import Stack

class StackSort(Stack):
    def __init__(self):
        super().__init__()
    
    def sort_stack(self):
        aux_stack = StackSort()
        while not self.is_empty():
            current = self.pop()
            while not aux_stack.is_empty() and aux_stack.peek() > current:
                self.push(aux_stack.pop())
            aux_stack.push(current)
        
        # Transfer back to original stack if needed
        while not aux_stack.is_empty():
            self.push(aux_stack.pop())


# Example usage
if __name__ == "__main__":
    my_stack = StackSort()
    my_stack.push(4)
    my_stack.push(1)
    my_stack.push(3)
    my_stack.push(2)

    print("Original Stack:")
    my_stack.print_stack()

    my_stack.sort_stack()
    print("Sorted Stack:")
    my_stack.print_stack()
    