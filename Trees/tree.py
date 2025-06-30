class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
        else:
            self.__insert_recursive(self.root, new_node)

    def __insert_recursive(self, current, new_node):
        if current is None:
            return new_node
        if new_node.value < current.value:
            current.left = self.__insert_recursive(current.left, new_node)
        else:
            current.right = self.__insert_recursive(current.right, new_node)
        return current
    
    def contains(self, value):
        return self.__contains_recursive(self.root, value)
    
    def __contains_recursive(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self.__contains_recursive(current.left, value)
        else:
            return self.__contains_recursive(current.right, value)
    
    def inorder(self):
        elements = []
        self.__inorder_recursive(self.root, elements)
        print("->".join(map(str, elements)))
    
    def __inorder_recursive(self, current, elements):
        if current:
            self.__inorder_recursive(current.left, elements)
            elements.append(current.value)
            self.__inorder_recursive(current.right, elements)

    def preorder(self):
        elements = []
        self.__preorder_recursive(self.root, elements)
        print('->'.join(map(str, elements)))

    def __preorder_recursive(self, current, elements):
        if current:
            elements.append(current.value)
            self.__preorder_recursive(current.left, elements)
            self.__preorder_recursive(current.right, elements)
        
    def postorder(self):
        elements = []
        self.__postorder_recursive(self.root, elements)
        print('->'.join(map(str, elements)))

    def __postorder_recursive(self, current, elements):
        if current:
            self.__postorder_recursive(current.left, elements)
            self.__postorder_recursive(current.right, elements)
            elements.append(current.value)

        
# Example usage
if __name__ == "__main__":
    tree = Tree()
    print("Inserting values into the tree:")
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)


    print("\nIs 3 a part of the tree: ",tree.contains(3))  # Output: True
    print("Is 4 a part of the tree: ",tree.contains(4))  # Output: False

    print("\nInorder traversal of the tree: ", end="")
    tree.inorder()  # Output: 3->5->7->

    print("Preorder traversal of the tree: ", end="")
    tree.preorder()  # Output: 5->3->7->

    print("Postorder traversal of the tree: ", end="")
    tree.postorder()  # Output: 3->7->5->