class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
    
    def pop(self):
        temp=self.head
        bef=self.head
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            self.length-=1
            return temp.value
        while temp.next is not None:
            bef=temp
            temp=temp.next
        self.tail=bef
        self.tail.next=None
        temp.prev=None
        self.length-=1
        return temp
    
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            self.length+=1
            return True
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        self.length+=1

    def Pop_First(self):
        if self.length==0:
            print("no items in dll")
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp
    
    def Get(self,index):
        if index<0 or index>=self.length:
            print("invalid index")
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp

    def Set(self,index,value):
        if index<0 or index>=self.length:
             print("invalid index")
             return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        temp.value=value
        return True

    def insert(self,index,value):
        if index<0 or index>self.length:
             print("invalid index")
             return None
        if index==0:
            self.prepend(value)
            return True
        if index==self.length:
            self.append(value)
            return True
        new_node=Node(value)
        temp=self.Get(index)
        bef=temp.prev
        bef.next=new_node
        new_node.next=temp
        temp.prev=new_node
        new_node.prev=bef
        self.length+=1
        return True
    
    def remove(self,index):
        if index<0 or index>=self.length:
            print("invalid index")
            return None
        if index==0:
            temp=self.Pop_First()
            return temp
        if index==self.length-1:
            temp=self.pop()
            return True
        temp=self.Get(index)
        bef=temp.prev
        bef.next=temp.next
        temp.next.prev=bef
        temp.next=None
        temp.prev=None
        self.length-=1
        return temp


    def print(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

my_dll=DoublyLinkedList(6)
my_dll.append(7)
my_dll.append(8)
my_dll.prepend(5)
my_dll.remove(3)
my_dll.print()
