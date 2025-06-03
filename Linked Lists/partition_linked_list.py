from linked_list import LinkedList, Node

class PartitionedLinkedList(LinkedList):
    def partition_list(self, x):
        """
        Partitions the linked list around a value x, such that all nodes less than x come before nodes greater than or equal to x.
        The original relative order of the nodes is preserved.
        """
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
        
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        prev1.next = dummy2.next
        prev2.next = None
        
        self.head = dummy1.next

# Example usage
if __name__ == "__main__":
    ll = PartitionedLinkedList(3)
    ll.append(5)
    ll.append(8)
    ll.append(5)
    ll.append(10)
    ll.append(2)
    ll.append(1)

    print("Original list:")
    ll.print_list()

    partition_value = 5
    ll.partition_list(partition_value)

    print(f"Partitioned list around {partition_value}:")
    ll.print_list()