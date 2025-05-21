from linked_list import LinkedList

class ExtendedLinkedList(LinkedList):
    def __init__(self, value):
        super().__init__(value)
    
    def has_loop(self):
        if self.length == 0:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            print(f"Slow: {slow.value}, Fast: {fast.value}")
            if slow == fast:
                return True
        return False
    
my_linked_list = ExtendedLinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.head.next.next.next.next.next = my_linked_list.head.next  # Creating a loop for testing
print("Has loop:", my_linked_list.has_loop())  # Output: True