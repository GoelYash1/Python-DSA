from double_linked_list import DoublyLinkedList, Node

class PartitionDoublyLinkedList(DoublyLinkedList):
    def partition(self, x):
        if not self.head or not self.tail:
            return 
        curr = self.head
        dummy1 = Node(0)
        dummy2 = Node(0)
        less = dummy1
        greater = dummy2

        while curr:
            if curr.value < x:
                less.next = curr
                curr.prev = less
                less = curr
            else:
                greater.next = curr
                curr.prev = greater
                greater = curr
            curr = curr.next

        self.head = dummy1.next
        if self.head:
            self.head.prev = None
        less.next = dummy2.next
        if dummy2.next:
            dummy2.next.prev = less

        self.tail = greater
        greater.next = None
        if not self.tail:
            self.tail = less
        
# Example usage
if __name__ == "__main__":
    my_doubly_linked_list = PartitionDoublyLinkedList(3)
    my_doubly_linked_list.append(5)
    my_doubly_linked_list.append(8)
    my_doubly_linked_list.append(5)
    my_doubly_linked_list.append(10)
    my_doubly_linked_list.append(2)
    my_doubly_linked_list.append(1)

    print("Original list:")
    my_doubly_linked_list.print_list()

    my_doubly_linked_list.partition(5)
    print("\nPartitioned list (less than 5 on the left):")
    my_doubly_linked_list.print_list()

    print("\nHead:", my_doubly_linked_list.head.value if my_doubly_linked_list.head else None)
    print("Tail:", my_doubly_linked_list.tail.value if my_doubly_linked_list.tail else None)