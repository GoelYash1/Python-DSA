from linked_list import LinkedList, Node

class SwapPairsLinkedList(LinkedList):
    def swap_pairs(self):
        """
        Swaps every two adjacent nodes in the linked list.
        If the list has an odd number of nodes, the last node remains unchanged.
        """
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        current = self.head
        
        while current and current.next:
            first = current
            second = current.next
            
            # Swap the nodes
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move pointers forward
            prev = first
            current = first.next
        
        self.head = dummy.next

# Example usage
if __name__ == "__main__":
    ll = SwapPairsLinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    print("Original list:")
    ll.print_list()

    ll.swap_pairs()

    print("List after swapping nodes:")
    ll.print_list()