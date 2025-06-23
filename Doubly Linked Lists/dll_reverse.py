from double_linked_list import DoublyLinkedList

class ReverseDoublyLinkedList(DoublyLinkedList):
    def reverse(self):
        temp = self.head
        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
        self.head, self.tail = self.tail, self.head
        
my_doubly_linked_list = ReverseDoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)

print("Original list:")
my_doubly_linked_list.print_list()

my_doubly_linked_list.reverse()
print("\nReversed list:")
my_doubly_linked_list.print_list()
