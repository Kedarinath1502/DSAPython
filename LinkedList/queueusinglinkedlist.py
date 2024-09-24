class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    
    def enqueue(self,value):
        new_node=Node(value)
        if self.length==0:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1
    
    def dequeue(self):
        if self.length==0:
            print("no elements in queue")
            return None
        temp=self.first
        self.first=self.first.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.last=None
        return temp
    
    def print(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
        
my_queue=Queue(2)
my_queue.enqueue(3)
my_queue.dequeue()
my_queue.dequeue()
my_queue.enqueue(3)


my_queue.print()
