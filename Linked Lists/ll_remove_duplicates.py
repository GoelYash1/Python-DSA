from linked_list import LinkedList

class ExtendedLinkedList(LinkedList):
    def __init__(self, value):
        super().__init__(value)

    def remove_duplicates(self):
            values = set()
            previous = None
            current = self.head
            while current:
                if current.value in values:
                    previous.next = current.next
                    self.length -= 1
                else:
                    values.add(current.value)
                    previous = current
                current = current.next
                
# Example usage
my_linked_list = ExtendedLinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(3)

print("Original list:")
my_linked_list.print_list()

my_linked_list.remove_duplicates()

print("List after removing duplicates:")
my_linked_list.print_list()