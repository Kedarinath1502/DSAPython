class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else : 
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def print(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        bef=None
        while temp is not None:
            aft=temp.next
            temp.next=bef
            bef=temp
            temp=aft
            
        



my_ll=LinkedList(5)
my_ll.append(4)
my_ll.append(3)
my_ll.append(2)
my_ll.append(1)
my_ll.reverse()
my_ll.print()
        