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
    
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
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
    
    def pop_first(self):
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            index = self.length - 1 - index
            for _ in range(index):
                current = current.prev
        return current
    
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

# Prepending values to the doubly linked list
print("Prepending values to the doubly linked list:")
my_doublely_linked_list.prepend(0)
my_doublely_linked_list.prepend(-1)
my_doublely_linked_list.print_list()

# Popping the first value from the doubly linked list
print("Popping the first value from the doubly linked list:")
popped_first_node = my_doublely_linked_list.pop_first()
if popped_first_node:
    print(f"Popped first value: {popped_first_node.value}")
    my_doublely_linked_list.print_list()

# Getting a node at a specific index
print("Getting node at index 1:")
node_at_index = my_doublely_linked_list.get(1)
if node_at_index:
    print(f"Node at index 1: {node_at_index.value}")

# Getting a node from second half of the list
print("Getting node from the 2nd half of the list:")
node_at_2nd_index = my_doublely_linked_list.get(2)
if node_at_2nd_index:
    print(f"Node at 2nd index: {node_at_2nd_index.value}")

