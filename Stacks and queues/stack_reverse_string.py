from stack import Stack

class ReverseStringStack(Stack):
    def reverse_string(self, input_string):
        for char in input_string:
            self.push(char)
        
        reversed_string = ""
        while not self.is_empty():
            reversed_string += self.pop()
        
        return reversed_string

# Example usage
if __name__ == "__main__":
    my_stack = ReverseStringStack()
    input_string = "Hello, World!"
    
    reversed_string = my_stack.reverse_string(input_string)
    print("Original String:", input_string)
    print("Reversed String:", reversed_string)
