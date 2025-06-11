class Node:
    def __init__(self, value):
        self.value= value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if not self.head:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = popped_node.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" <-> " if current.next else "\n")
            current = current.next

# Initializing the doubly linked list with a single value
my_doublely_linked_list = DoublyLinkedList(1)

print("Initial doubly linked list:")
my_doublely_linked_list.print_list()

# Appending values to the doubly linked list
print("Appending values to the doubly linked list:")
my_doublely_linked_list.append(2)
my_doublely_linked_list.append(3)
my_doublely_linked_list.append(4)

my_doublely_linked_list.print_list()

# Popping the last value from the doubly linked list
print("Popping the last value from the doubly linked list:")
popped_node = my_doublely_linked_list.pop()

if popped_node:
    print(f"Popped value: {popped_node.value}")
    my_doublely_linked_list.print_list()

