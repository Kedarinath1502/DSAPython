class maxHeap:
    def __init__(self):
        self.heap = []
    
    def left_child(self,index):
        return 2 * index + 1
    
    def right_child(self,index):
        return 2 * index + 2
    
    def parent(self, index):
        return (index - 1) // 2
    
    def swap(self, index1, index2):
        self.heap[index1] , self.heap[index2] = self.heap[index2] , self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        while (index != 0 and self.heap[index] > self.heap[self.parent(index)]):
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def print_heap(self):
        print(self.heap)
    
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sinkdown(0)

        return max_value
    
    def sinkdown(self,index):
        max_index = index
        while True:
            left_index = self.left_child(index)
            right_index = self.right_child(index)

            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
            
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            
            if max_index != index:
                self.swap(max_index, index)
                index = max_index
            else:
                return

maxheap = maxHeap()
maxheap.insert(99)
maxheap.insert(58)
maxheap.insert(72)
maxheap.insert(61)
maxheap.insert(100)
maxheap.remove()
maxheap.print_heap()

