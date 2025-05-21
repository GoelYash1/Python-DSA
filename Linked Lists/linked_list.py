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

    def prepend(self, value):
        new_node = Node(value)
        if self.length ==0:
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.length += 1
        return True

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
    
    def pop_first(self):
        if self.length == 0:
            return Node(None)
        current_node = self.head
        self.head = self.head.next
        current_node.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return current_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return Node(None)
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        current = self.head
        for _ in range(index - 1):
            current = current.next
        removed_node = current.next
        current.next = removed_node.next
        removed_node.next = None
        self.length -= 1
        return removed_node
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return Node(None)
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        temp = self.get(index)
        if temp.value is None:
            return False
        temp.value = value
        return True

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.value,end=" -> ")
            current = current.next
        print("\n")