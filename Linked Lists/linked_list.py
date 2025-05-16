class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return Node(None)
        if self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node
        
        current  = self.head
        while current.next.next is not None:
            current = current.next
        popped_node = current.next
        current.next = None
        self.tail = current
        self.length -= 1
        return popped_node

    def insert(self, value, index):
        pass

    def remove(self, index):
        pass

    def prepend(self, value):
        new_node = Node(value)
        if self.length ==0:
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node
        self.length += 1

    def print_list(self):
        current = self.head
        while current:
            print(current.value,end=" -> ")
            current = current.next

# Create a linked list and test the methods
my_linked_list = LinkedList(4)

# Append some values
my_linked_list.append(5)
my_linked_list.append(6)

# Prepend some values
my_linked_list.prepend(3)
my_linked_list.prepend(2)
my_linked_list.prepend(1)

# Print the list
my_linked_list.print_list()

# Pop some values
print("\nPopped:", my_linked_list.pop().value)
my_linked_list.print_list()

# Pop again
print("\nPopped:", my_linked_list.pop().value)
my_linked_list.print_list()

# Pop again
print("\nPopped:", my_linked_list.pop().value)
my_linked_list.print_list()