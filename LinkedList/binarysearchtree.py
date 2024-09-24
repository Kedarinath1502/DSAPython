class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
    
    def insert(self, value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while True:
            if value==temp.value:
                return False
            if value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right



    
        
    
    def print(self):
        print(self.root.right.value)

mytree=BinarySearchTree()
print(mytree.insert(42))
print(mytree.insert(44))
print(mytree.insert(24))
print(mytree.insert(21))
print(mytree.print())