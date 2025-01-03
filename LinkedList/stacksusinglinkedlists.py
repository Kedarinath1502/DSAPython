class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
    
    def push(self,value):
        new_node=Node(value)
        if self.height==0:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1
        return True
    
    def Pop(self):
        if self.height==0:
            print("no elements in stack")
            return None
        else:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            self.height-=1
            return temp
    
    def print(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next


        
my_stack=Stack(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.Pop()
my_stack.Pop()
my_stack.Pop()

my_stack.print()