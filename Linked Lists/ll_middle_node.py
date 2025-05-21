from linked_list import LinkedList

class ExtendedLinkedList(LinkedList):
    def __init__(self, value):
        super().__init__(value)
    
    def middle_node(self):
        if self.length == 0:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
my_linked_list = ExtendedLinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print("Middle node value:", my_linked_list.middle_node().value)  # Output: 3