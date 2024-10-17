class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def lookup(self, value):
        # if self.root is None:
        #     return False
        temp = self.root
        # while True:
        #     if temp.value == value:
        #         return True
        #     elif temp.value > value:
        #         temp = temp.left
        #         if temp is None:
        #             return False
        #     else:
        #         temp = temp.right
        #         if temp is None: 
        #             return False
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        
        

bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)

print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)
print(bst.lookup(3))
print(bst.lookup(4))
print(bst.lookup(1))
print(bst.lookup(2))


                    
