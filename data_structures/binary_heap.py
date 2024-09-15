"""
File: binary_heap.py

Author: Anjola Aina
Date Modified: September 15th, 2024

This file contains a class representing a binary max heap, along with common heap operations.
"""
class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def parent(self, i: int) -> int:
        """
        Returns the parent node of the given child node.

        Args:
            i (int): The child node.

        Returns:
            int: The parent of the given child node.
        """
        return (i - 1) // 2
    
    def left(self, i: int) -> int:
        """
        Returns the left child of the given parent node.

        Args:
            i (int): The parent node.

        Returns:
            int: The left child of the parent node.
        """
        return (2 * i) + 1
    
    def right(self, i: int) -> int:
        """
        Returns the right child of the given parent node.

        Args:
            i (int): The parent node.

        Returns:
            int: The right child of the parent node.
        """
        return (2 * i) + 2
    
    def is_empty(self) -> bool:
        return len(self.heap) == 0 # If heap_size is 0, return True; otherwise, return False
    
    def build_max_heap(self, x: list[int]) -> None:
        """
        Builds a max heap from the given array.

        Args:
            x (list[int]): The input array to be converted into a max heap.
        """
        self.heap = x
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i, len(self.heap))
    
    def get_max(self) -> int:
        """
        Gets the maximum element of a heap.

        Raises:
            RuntimeError: Occurs when the heap is empty.

        Returns:
            int: The maximum element of a heap.
        """
        if not self.is_empty():
            return self.heap[0]
        else:
            raise RuntimeError('Cannot get the maximum item from an empty heap.')
        
    def extract_max(self) -> int:
        """
        Removes and returns the maximum element of a heap.

        Raises:
            RuntimeError: Occurs when the heap is empty.

        Returns:
            int: The maximum element of a heap.
        """
        if self.is_empty():
            raise RuntimeError('Cannot extract the maximum item from an empty heap.')
        
        if len(self.heap) == 1:
            key = self.heap.pop()
            return key
        
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max = self.heap.pop()
        # Heapify from the root to restore the heap property
        self.heapify(0, len(self.heap)) 
        return max
    
    def remove(self, i: int) -> int:
        """
        Removes and returns an element from the heap.

        Args:
            i (int): The index of the element to be removed.

        Raises:
            RuntimeError: Occurs when the heap is empty.
            IndexError: Occurs when the index is less than 0 or greater than the heap size.

        Returns:
            int: The removed element.
        """
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
    
    def heapify(self, i: int, heap_size: int) -> None:
        """
        Implements the heapify algorithm to satisify the max heap property.

        Args:
            i (int): The index to start the heapify process.
            heap_size (int): The size of the heap.
        """
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
            
    def insert(self, val: int) -> None:
        """
        Inserts an element into its correct location in the heap.

        Args:
            val (int): The value to be inserted into the heap.
        """
        self.heap.append(val)
        self._shift_up(len(self.heap) - 1) 
        
    def _shift_up(self, i):
        """
        Places a value in its correct location in the heap.

        Args:
            i (int): The index of the value to be shifted up. 
        """
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
            
    def _increase_val(self, i: int, new_val: int) -> None:
        """
        Increases the value of an element in the heap.

        Args:
            i (int): The index of the element to be changed.
            new_val (int): The new value of the element.
        """
        self.heap[i] = new_val
        self._shift_up(i)
        
    def _decrease_val(self, i: int, new_val: int) -> None:
        """
        Decreases the value of an element in the heap.

        Args:
            i (int): The index of the element to be changed.
            new_val (int): The new value of the element.
        """
        self.heap[i] = new_val
        self.heapify(i, len(self.heap))
        
    def change_val(self, i: int, new_val: int) -> None:
        """
        Changes the value of an element in the heap.

        Args:
            i (int): The index of the element to be changed.
            new_val (int): The new value of the element.

        Raises:
            IndexError: Occurs when the index is less than 0 or greater than the heap size.
        """
        if i >= len(self.heap) or i < 0: 
            raise IndexError(f'Index {i} out of bounds for a heap of size: {len(self.heap)}.')
        if self.heap[i] == new_val:
            return
        
        if self.heap[i] < new_val:
            self._increase_val(i, new_val)
        else:
            self._decrease_val(i, new_val)
        
    def print_heap(self) -> None:
        """
        Prints the heap.
        """
        print(self.heap)