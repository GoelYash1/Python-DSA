from double_linked_list import DoublyLinkedList, Node

class ReverseBetweenDoublyLinkedList(DoublyLinkedList):
    def reverse_between(self, start_index, end_index):
        if self.length <= 1 or start_index == end_index:
            return
 
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
 
        prev = dummy
        for _ in range(start_index):
            prev = prev.next
 
        current = prev.next
 
        for _ in range(end_index - start_index):
            node_to_move = current.next
 
            current.next = node_to_move.next
            if node_to_move.next:
                node_to_move.next.prev = current
 
            node_to_move.next = prev.next
            prev.next.prev = node_to_move
            prev.next = node_to_move
            node_to_move.prev = prev
 
        self.head = dummy.next
        self.head.prev = None
        

# Example usage
if __name__ == "__main__":
    my_doubly_linked_list = ReverseBetweenDoublyLinkedList(1)
    my_doubly_linked_list.append(2)
    my_doubly_linked_list.append(3)
    my_doubly_linked_list.append(4)
    my_doubly_linked_list.append(5)

    print("Original list:")
    my_doubly_linked_list.print_list()

    my_doubly_linked_list.reverse_between(2, 4)
    print("\nReversed sublist from 2 to 4:")
    my_doubly_linked_list.print_list()