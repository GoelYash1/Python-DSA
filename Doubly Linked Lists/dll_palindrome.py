from double_linked_list import DoublyLinkedList

class PalindromeCheckDoublyLinkedList(DoublyLinkedList):
    def is_palindrome(self):
        if self.length == 0:
            return True
        
        left = self.head
        right = self.tail
        
        for _ in range(self.length // 2):
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev
        
        return True

my_doubly_linked_list = PalindromeCheckDoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(1)

print("List contents:")
my_doubly_linked_list.print_list()
print("Is the list a palindrome?", my_doubly_linked_list.is_palindrome())

my_doubly_linked_list.append(4)
print("\nAfter appending 4:")
my_doubly_linked_list.print_list()
print("Is the list a palindrome?", my_doubly_linked_list.is_palindrome())