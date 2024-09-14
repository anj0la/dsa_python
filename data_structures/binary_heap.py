class MaxHeap:
    def __init__(self, heap_size):
        self.heap = [0] * heap_size
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return (2 * i) + 1
    
    def right(self, i):
        return (2 * i) + 2
    
    def is_empty(self):
        return len(self.heap) == 0 # If heap_size is 0, return True; otherwise, return False
    
    def get_max(self):
        if not self.is_empty():
            return self.heap[0]
        else:
            raise RuntimeError('Cannot get the maximum item from an empty heap.')
        
    def extract_max(self):
        if self.is_empty():
            raise RuntimeError('Cannot extract the maximum item from an empty heap.')
        
        if len(self.heap) == 1:
            key = self.heap.pop()
            return key
        
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        max = self.heap.pop()
        self.heapify(0, len(self.heap)) # Max heapify down from the root to fix max heap property
        return max
    
    def remove(self, i):
        if self.is_empty():
            raise RuntimeError('Cannot extract the maximum item from an empty heap.')
        
        if len(self.heap) == 1:
            key = self.heap.pop()
            return key
        
        if i >= len(self.heap) or i < 0: 
            raise IndexError(f'Index {i} out of bounds for a heap of size: {len(self.heap)}.')
        
        # It is assumed heap is a max heap, so the map heap property is satisfied
        if i == len(self.heap) - 1: 
            return self.heap.pop()
        else:
            self.heap[i], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[i]
            key = self.heap.pop()
            self.heapify(i, len(self.heap)) # Max heapify down from i to fix max heap property
            return key
    
    def heapify(self, i, heap_size):
        left = self.left(i)
        right = self.right(i)
        largest = i
        
        if left < heap_size and self.heap[left] > self.heap[i]:
            largest = left
            
        if right < heap_size and self.heap[right] > self.heap[largest]:
            largest = right
            
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i] 
            self.heapify(largest, heap_size)
            
    def insert(self, val):
        self.heap.append(val)
        self.shift_up(len(self.heap) - 1) 
        
    def shift_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
            
    def increase_val(self, i, new_val):
        self.heap[i] = new_val
        self.shift_up(i)
        
    def decrease_val(self, i, new_val):
        self.heap[i] = new_val
        self.heapify(i, len(self.heap))
        
    def change_val(self, i, new_val):
        if i >= len(self.heap) or i < 0: 
            raise IndexError(f'Index {i} out of bounds for a heap of size: {len(self.heap)}.')
        if self.heap[i] == new_val:
            return
        
        if self.heap[i] < new_val:
            self.increase_val(i, new_val)
        else:
            self.decrease_val(i, new_val)
        
    def print_heap(self):
        print(self.heap)
            