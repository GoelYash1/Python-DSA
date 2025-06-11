from linked_list import LinkedList, Node

class ReverseBetweenLinkedList(LinkedList):
    def reverse_between(self, left, right):
        """
        Reverses the linked list from position left to right (0-indexed).
        """
        if left == right:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
        # Move prev to the node just before the left position
        for _ in range(left):
            prev = prev.next
        
        # Start reversing
        current = prev.next
        tail = current
        
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev.next
            prev.next = current
            current = next_node
           
        tail.next = current
        self.head = dummy.next

# Example usage
if __name__ == "__main__":
    ll = ReverseBetweenLinkedList(1)
    ll.append(4)
    ll.append(3)
    ll.append(2)
    ll.append(5)

    print("Original list:")
    ll.print_list()

    left, right = 1, 3
    ll.reverse_between(left, right)

    print(f"List after reversing between positions {left} and {right}:")
    ll.print_list()