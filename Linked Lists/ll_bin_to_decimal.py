from linked_list import LinkedList

class extended_linked_list(LinkedList):
    def __init__(self, value):
        super().__init__(value)
    
    def bin_to_decimal(self):
        num = 0
        current = self.head
        
        while current:
            num = num*2 + current.value
            current = current.next
        return num
    
my_linked_list = extended_linked_list(1)
my_linked_list.append(0)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(0)

print("Binary to Decimal value:", my_linked_list.bin_to_decimal())