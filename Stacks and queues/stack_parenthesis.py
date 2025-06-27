from stack import Stack

class ParenthesisStack(Stack):
    def __init__(self):
        super().__init__()

    def is_balanced(self, expression):
        for char in expression:
            if char == "(":
                self.push(char)
            elif char == ")":
                if self.is_empty():
                    return False
                self.pop()
        return self.is_empty()

# Example usage
if __name__ == "__main__":
    my_stack = ParenthesisStack()
    expression = "(()())"

    if my_stack.is_balanced(expression):
        print(f"The expression '{expression}' is balanced.")
    else:
        print(f"The expression '{expression}' is not balanced.")

# Example usage with unbalanced expression
    expression = "(()"
    if my_stack.is_balanced(expression):
        print(f"The expression '{expression}' is balanced.")
    else:  
        print(f"The expression '{expression}' is not balanced.")


