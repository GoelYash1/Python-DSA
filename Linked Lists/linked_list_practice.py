from linked_list import LinkedList

# Create a linked list and test the methods
my_linked_list = LinkedList(4)

# Append some values
my_linked_list.append(5)
my_linked_list.append(6)
print("After appending:")
my_linked_list.print_list()

# Prepend some values
my_linked_list.prepend(3)
my_linked_list.prepend(2)
my_linked_list.prepend(1)
print("After prepending:")
my_linked_list.print_list()

# Insert some values
my_linked_list.insert(1,10)
print("After inserting at indexition 1:")
my_linked_list.print_list()

# Insert at a random indexition
my_linked_list.insert(3,20)
print("After inserting at indexition 3:")
my_linked_list.print_list()

# Insert at the end
my_linked_list.insert(10,30)
print("After inserting at indexition 10 (out of index):")
my_linked_list.print_list()

# reverse the linked list
print("Reversing the linked list:")
my_linked_list.reverse()
my_linked_list.print_list()

# Pop some values
print("Popped:", my_linked_list.pop().value)
my_linked_list.print_list()

# Pop again
print("Popped:", my_linked_list.pop().value)
my_linked_list.print_list()

# Pop again
print("Popped:", my_linked_list.pop().value)
my_linked_list.print_list()

# Pop first
print("Popped first:", my_linked_list.pop_first().value)
my_linked_list.print_list()

# Remove at index 1
print("Removed at index 1:", my_linked_list.remove(1).value)
my_linked_list.print_list()

# Remove at index 0
print("Removed at index 0:", my_linked_list.remove(0).value)
my_linked_list.print_list()

# Remove at index 1
print("Removed at index 1:", my_linked_list.remove(1).value)
my_linked_list.print_list()

# Append some values
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.append(9)
print("After appending:")
my_linked_list.print_list()

# get some values
print("Get at index 0:", my_linked_list.get(0).value)
print("Get at index 1:", my_linked_list.get(1).value)

# set value at index 2
print("Set at index 2:", my_linked_list.set_value(2, 100))
print("After setting at index 2:")
my_linked_list.print_list()