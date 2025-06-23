class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        self.top = Node(value)
        self.height = 1
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
    
    def pop(self):
        if self.height == 0:
            raise IndexError("Pop from empty stack")
        popped_value = self.top.value
        self.top = self.top.next
        self.height -= 1
        return popped_value
    
    def print_stack(self):
        current = self.top
        while current:
            print(current.value, end="->")
            current = current.next
        print()


# example usage
if __name__ == "__main__":
    my_stack = Stack(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)

    print("Stack height:", my_stack.height)
    print("Stack contents:")
    my_stack.print_stack()

    print("Top element:", my_stack.top.value)

    popped_value = my_stack.pop()
    print("Popped value:", popped_value)
    print("Stack height after pop:", my_stack.height)
    print("Stack contents after pop:")
    my_stack.print_stack()
        