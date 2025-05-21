from linked_list import LinkedList

def kth_node_from_end(ll, k):
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
k = 2
kth_node = kth_node_from_end(my_linked_list,k)
if kth_node:
    print(f"The {k}th node from the end is: {kth_node.value}")  # Output: 4
else:
    print(f"The list is shorter than {k} nodes.")