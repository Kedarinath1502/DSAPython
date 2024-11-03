class minHeap:
    def __init__(self):
        self.heap = []
    
    def left_child(self, index):
        return 2 * index + 1
    
    def right_child(self, index):
        return 2 * index + 2
    
    def parent(self, index):
        return (index - 1) // 2
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        while index != 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def print_heap(self):
        print(self.heap)
    
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sinkdown(0)

        return min_value
    
    def sinkdown(self, index):
        min_index = index
        while True:
            left_index = self.left_child(index)
            right_index = self.right_child(index)

            if left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]:
                min_index = left_index
            
            if right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]:
                min_index = right_index
            
            if min_index != index:
                self.swap(min_index, index)
                index = min_index
            else:
                return

minheap = minHeap()
minheap.insert(99)
minheap.insert(58)
minheap.insert(72)
minheap.insert(61)
minheap.insert(100)
minheap.remove()
minheap.print_heap()
