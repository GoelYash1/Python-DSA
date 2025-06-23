from double_linked_list import DoublyLinkedList, Node

class SwapPairsDoublyLinkedList(DoublyLinkedList):
    def swap_pairs(self):
        if self.length <= 1:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        if self.head:
            self.head.prev = dummy
        
        prev = dummy
        current = self.head
        
        while current and current.next:
            first = current
            second = current.next
            
            # Swapping the nodes
            first.next = second.next
            if second.next:
                second.next.prev = first
            
            second.prev = prev
            prev.next = second
            second.next = first
            first.prev = second
            
            # Move to the next pair
            prev = first
            current = first.next
        
        self.head = dummy.next
        if self.head:
            self.head.prev = None

# Example usage
if __name__ == "__main__":
    my_doubly_linked_list = SwapPairsDoublyLinkedList(1)
    my_doubly_linked_list.append(2)
    my_doubly_linked_list.append(3)
    my_doubly_linked_list.append(4)
    my_doubly_linked_list.append(5)

    print("Original list:")
    my_doubly_linked_list.print_list()

    my_doubly_linked_list.swap_pairs()
    print("\nList after swapping pairs:")
    my_doubly_linked_list.print_list()