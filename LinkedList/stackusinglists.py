class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self,value):
        self.items.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def isEmpty(self):
        return len(self.items)==0
   
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None
        
    def print(self):
        print(self.items)

my_stack=Stack()

print(my_stack.pop())
my_stack.print()